
import os
from binascii import hexlify
from socket import error, inet_aton, inet_pton, socket
from socket import AF_INET
from socket import AF_INET6
from struct import unpack, unpack_from, error as struck_err
from IPQualityScore.Columns         import Column
from IPQualityScore.Exceptions      import FileReaderException
from IPQualityScore.Exceptions      import IPNotFoundException
from IPQualityScore.BinaryOption    import BinaryOption
from IPQualityScore.IPQSRecord      import IPQSRecord
import IPQualityScore.Utilities as Utilities

class DBReader:
    READER_VERSION = 1
    BASE_TREE_BYTES = 5
    TREE_BYTE_WIDTH = 4
    BASE_HEADER_BYTES = 11
    BINARY_DATA_HEADER = "<BBB"
    NONBINARY_DATA_HEADER = "<B"
    COLUNN_HEADER = "<P23xB" #"x%s/a23name/Cvalue" null 23null-padded_string UnsigedChar <x23xB
    HEADERS = "<BB3BHL"

    

    def __init__(self, filename:str):
        if not os.path.isfile(filename):
            raise FileReaderException('Invalid or nonexistent file name specified. Please check the file and try again')
        
        try:
            self.handler = open(filename,'rb')
        except IOError:
            raise FileReaderException('Invalid or nonexistent file name specified. Please check the file and try again')

        self.tree_start = None
        self.tree_end = None
        self.record_bytes = None
        self.columns = []
        self.ipv6 = False
        self.blacklistfile = False

        self.SetupHeaders()
        self.SetupColumns()
        self.SetupTreeHeaders()

    def Fetch(self, ip:str):
        if not self.IsIPv4(ip) and not self.IsIPv6(ip):
            raise FileReaderException("Attempted to look up invalid IP address. Aborting.")
        
        if self.ipv6 and not self.IsIPv6(ip):
            raise FileReaderException("Attempted to look up IPv4 using IPv6 database file. Aborting.")
        
        if self.ipv6 == False and not self.IsIPv4(ip):
            raise FileReaderException("Attempted to look up IPv6 using IPv4 database file. Aborting.")
        
        if self.ipv6 == False and ip.startswith("0."):
            raise FileReaderException("Attempted to look up an IP address in the 0.0.0.0/8 range. Aborting.")
        
        v_literal = self.IP2Literal(ip)
        position = 0
        previous = {}
        file_position  =  self.tree_start + self.BASE_TREE_BYTES

        # Loop over tree. Will abort if we try too many times.
        for _ in range(257):
            previous[position] = file_position
            if len(v_literal) <= position:
                raise IPNotFoundException("Invalid or nonexistent IP address specified for lookup. (EID: 8)")

            if v_literal[position] == 0:
                pos = self.ReadAt(file_position, self.TREE_BYTE_WIDTH)
                if len(pos) == 4:
                    file_position = unpack("<L", pos)[0]
            else:
                pos = self.ReadAt(file_position + 4, self.TREE_BYTE_WIDTH)
                if len(pos) == 4:
                    file_position = unpack("<L", pos)[0]

            if(self.blacklistfile == False):
                if(file_position == 0):
                    for i in range(position):
                        if(v_literal[position - i] == 1):
                            v_literal[position - i] = 0

                            for n in range(position - i + 1, len(v_literal)):
                                v_literal[n] = 1
                            
                            position = position - i
                            file_position = previous[position]
                            break
                    continue

            if(file_position < self.tree_end):
                if(file_position == 0):
                    break
                position += 1
                continue

            try:
                raw = self.ReadAt(file_position, self.record_bytes)
            except Exception:
                raise IPNotFoundException("Invalid or nonexistent IP address specified for lookup. (EID: 11)")

            try:
                return self.CreateRecord(raw)

            except Exception:
                raise IPNotFoundException("Invalid or nonexistent IP address specified for lookup. (EID: 12)")
        raise IPNotFoundException("Invalid or nonexistent IP address specified for lookup. (EID: 13)")
        
    def GetColumns(self):
        return self.columns

    def Read(self, blenght):
        try:
            data = self.handler.read(blenght)
        except IOError:
            raise IPNotFoundException("Unknown file format. Please check the file's integrity. EID 13")
        return data
    
    def ReadAt(self, position, b):
        self.handler.seek(position)
        d = self.handler.read(b)
        if d == False:
            raise IPNotFoundException("Unknown file format. Please check the file's integrity. EID 14")
        return d

    def SetupHeaders(self):
        try:
            headers ={}
            headers["file_type"], headers["version"], headers["header_bytes1"], headers["header_bytes2"], headers["header_bytes3"], headers["record_bytes"], headers["file_bytes"] = unpack(self.HEADERS, self.Read(self.BASE_HEADER_BYTES))
        except Exception:
            raise FileReaderException("Invalid file format, unable to read first 11 bytes. EID 1")
        if headers["file_type"] == None:
            raise FileReaderException("Invalid file format, unable to read first 11 bytes. EID 1")
        
        file_type = BinaryOption.Create(headers["file_type"])
        if file_type.Has(BinaryOption.IPV4MAP):
            self.valid = True
            self.ipv6 = False
        
        if file_type.Has(BinaryOption.IPV6MAP):
            self.valid = True
            self.ipv6 = True

        if file_type.Has(BinaryOption.BINARYDATA):
            self.binary_data = True

        if file_type.Has(BinaryOption.BLACKLISTFILE):
            self.blacklistfile = True
        
        if(self.valid == False):
            raise FileReaderException("Invalid file format, invalid first byte. EID 1.")
        
        if headers['version'] != DBReader.READER_VERSION:
            raise FileReaderException("Invalid file version, EID 2.")
        
        
        self.tree_start = Utilities.uVarInt([headers['header_bytes1'], headers['header_bytes2'], headers['header_bytes3']])
        if self.tree_start == 0:
            raise FileReaderException("Invalid file format, invalid header bytes. EID 2")
        
        if headers['record_bytes'] == 0:
            raise FileReaderException("Invalid file format, invalid record size. EID 3")
        
        self.record_bytes = headers['record_bytes']

        if headers['file_bytes'] == 0 :
            raise FileReaderException("Invalid file format, invalid file size. EID 3")
    
    def SetupColumns(self):
        length = self.tree_start - self.BASE_HEADER_BYTES
        column_data = self.Read(length)
        values = {}
        for i in range(0, int(length/24)):
            s = i * 24
            values['name'], values['value'] = unpack_from("<{0}x23sB".format(i*24), column_data)
            BO = BinaryOption.Create(values['value'])
            C = Column.Create(values['name'].decode("utf-8").rstrip('\x00'), BO)
            self.columns.append(C)
        if len(self.columns) == 0:
            raise FileReaderException("File does not appear to be valid, no column data found. EID: 5")
    
    def SetupTreeHeaders(self):
        tree = {}
        tree['header'], tree['tree_bytes'] = unpack("<BL", self.Read(5))

        if tree['tree_bytes'] == 0 or BinaryOption.Create(tree['header']).Has(BinaryOption.TREEDATA) == False:
            raise FileReaderException("File does not appear to be valid, bad binary tree. EID: 6")
        
        self.tree_end = tree['tree_bytes'] + self.tree_start
    
    def IP2Literal(self,ip):
        result = []
        if (self.ipv6):
            for block in self.Expand(ip).split(":"):
                for x in bin(int(block, 16))[2:].zfill(16) : result.append(int(x))
        else:
            for block in ip.split("."):
                for x in bin(int(block, 10))[2:].zfill(8) : result.append(int(x))
        return result

    def CreateRecord(self,raw):
        bdata = {}
        record = IPQSRecord()
        current_byte = 0
        bdata['one'], bdata["two"], bdata["three"] = unpack("{0}B".format(len(raw)), raw)[:3]
        if self.binary_data:
            record.ParseFirstByte(BinaryOption.Create(bdata['one']))
            record.ParseSecondByte(BinaryOption.Create(bdata['two']))
            
            third = BinaryOption.Create(bdata['three'])
            record.ConnectionTypeRaw(third)
            record.AbuseVelocityRaw(third)
            current_byte = 3
        else:
            first = BinaryOption.Create(bdata['one'])
            record.ConnectionTypeRaw(first)
            record.AbuseVelocityRaw(first)
            current_byte = 1
        
        for column in self.columns:
            value = ""
            if column.Name() == "ASN":
                value = unpack("<L", raw[current_byte:current_byte+4])[0]
                record.ASN(int(value))
                current_byte += 4

            elif column.Name() == "Latitude":
                value = unpack("<f", raw[current_byte:current_byte+4])[0]
                record.Latitude(float(value))
                current_byte += 4

            elif column.Name() == "Longitude":
                
                value = unpack("<f", raw[current_byte:current_byte+4])[0]
                record.Longitude(float(value))
                current_byte += 4

            elif column.Name() == "ZeroFraudScore":
                value = unpack("B", raw[current_byte:current_byte+1])[0]
                record.SetFraudScore(0, int(value))
                current_byte += 1

            elif column.Name() == "OneFraudScore":
                value = unpack("B", raw[current_byte:current_byte+1])[0]
                record.SetFraudScore(1, int(value))
                current_byte += 1

            else:
                if (column.Type()).Has(BinaryOption.STRINGDATA):
                    value = self.GetRangedStringValue(unpack("<L", raw[current_byte:current_byte+4])[0])
                    if type(value) == tuple:
                        value = value[0].decode('utf-8')
                    current_byte += 4
                    try:
                        m = getattr(record, column.Name())
                        m(value)
                    except AttributeError:
                        pass
            
            record.AddColumns(Column.Create(column.Name(),column.Type(), value))
        
        return record
    def GetRangedStringValue(self, position):
        b = unpack("<B", self.ReadAt(position, 1))[0]
        return unpack(("<{0}s".format(b)), self.Read(b))

    def Expand(self, ip):
            l_hex = list(hexlify(inet_pton(AF_INET6, ip)).decode("utf-8"))
            return''.join(l + ':' * (n % 4 == 3) for n, l in enumerate(l_hex))[:-1]

    def IsIPv4(self, ip:str):
        try:
            inet_pton(AF_INET, ip)
            return True

        except error:
            return False

    def IsIPv6(self, ip:str):
        try:
            inet_pton(AF_INET6, ip)
            return True

        except error:
            return False

    def __del__(self):
        if self.handler:
            self.handler.close()