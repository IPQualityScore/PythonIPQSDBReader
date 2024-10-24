from IPQualityScore.BinaryOption    import BinaryOption
from IPQualityScore.Columns         import Column

class IPQSRecord:
    def __init__(self):
        self.__fraudscore = {}
        self.__Columns = []  
        self.__IsProxy           = False
        self.__IsVPN             = False
        self.__IsTOR             = False
        self.__IsCrawler         = False
        self.__IsBot             = False
        self.__IsBlackListed     = False
        self.__IsPrivate         = False
        self.__IsMobile          = False
        self.__RecentAbuse       = False
        self.__HasOpenPorts      = False
        self.__IsHostingProvider = False
        self.__ActiveVPN         = False
        self.__ActiveTOR         = False
        self.__PublicAccessPoint = False
        self.__ConnectionType    = 0
        self.__AbuseVelocity     = 0
        self.__fraudscore        = {}
        self.__Country           = ""
        self.__City              = ""
        self.__Region            = ""
        self.__ISP               = ""
        self.__Organization      = ""
        self.__Timezone          = ""
        self.__Latitude          = 0.0
        self.__Longitude         = 0.0
        self.__ASN               = 0

    def IsProxy(self, value = None):
        if value != None:
           self.__IsProxy = value
        return self.__IsProxy
    
    def IsVPN(self, value = None):
        if value != None:
           self.__IsVPN = value
        return self.__IsVPN
    
    def IsTOR(self, value = None):
        if value != None:
           self.__IsTOR = value
        return self.__IsTOR
    
    def IsCrawler(self, value = None):
        if value != None:
            self.__IsCrawler = value
        return self.__IsCrawler
    
    def IsBot(self, value = None):
        if value != None:
            self.__IsBot = value
        return self.__IsBot
    
    def IsBlackListed(self, value = None):
        if value != None:
            self.__IsBlackListed = value
        return self.__IsBlackListed

    def IsPrivate(self, value = None):
        if value != None:
            self.__IsPrivate = value
        return self.__IsPrivate
    
    def IsMobile(self, value = None):
        if value != None:
            self.__IsMobile = value
        return self.__IsMobile

    def RecentAbuse(self, value = None):
        if value != None:
            self.__RecentAbuse = value
        return self.__RecentAbuse
    
    def HasOpenPorts(self, value = None):
        if value != None:
            self.__HasOpenPorts = value
        return self.__HasOpenPorts
    
    def IsHostingProvider(self, value = None):
        if value != None:
            self.__IsHostingProvider = value
        return self.__IsHostingProvider

    def ActiveVPN(self, value = None):
        if value != None:
            self.__ActiveVPN = value
        return self.__ActiveVPN
    
    def ActiveTOR(self, value = None):
        if value != None:
            self.__ActiveTOR = value
        return self.__ActiveTOR

    def PublicAccessPoint(self, value = None):
        if value != None:
            self.__PublicAccessPoint = value
        return self.__PublicAccessPoint

    def ConnectionTypeRaw(self, value = None):
        if value != None:
            self.__ConnectionTypeRaw = self.ConvertConnectionType(value)
        return self.__ConnectionTypeRaw
    
    def ConnectionType(self, value:BinaryOption = None):
        if value != None:
            self.__ConnectionTypeRaw = self.ConvertConnectionType(value)
        
        items = {
            1: "Residential",
            2: "Mobile",
            3: "Corporate",
            4: "Data Center",
            5: "Education"
        }

        if(self.__ConnectionTypeRaw in items):
            return items[self.__ConnectionTypeRaw]
        else:
            return "Unknown"
    
    def FraudScore(self, strictness:int = 0, value = None):
        if value != None:
            self.__fraudscore[strictness] = value
        return self.__fraudscore[strictness]
    
    def SetFraudScore(self,strictness:int, value):
        self.__fraudscore[strictness] = value
    
    def AbuseVelocityRaw(self, value:BinaryOption = None):
        if value != None:
            self.__AbuseVelocity = value
        return self.__AbuseVelocity
    
    def AbuseVelocity(self, value:BinaryOption = None):
        if value != None:
            self.__AbuseVelocity = self.ConvertAbuseVelocity(value)
        items = {
            1: "low",
            2: "medium",
            3: "high",
        }
        if self.__AbuseVelocity in items:
            return items[self.__AbuseVelocity]
        else:
            return "none"
    
    def Country(self, value = None):
        if value != None:
            self.__Country = value
        return self.__Country
    
    def City(self, value = None):
        if value != None:
            self.__City = value
        return self.__City
    
    def Region(self, value = None):
        if value != None:
            self.__Region = value
        return self.__Region
    
    def ISP(self, value = None):
        if value != None:
            self.__ISP = value
        return self.__ISP
    
    def Organization(self, value = None):
        if value != None:
            self.__Organization = value
        return self.__Organization
    
    def Zipcode(self, value = None):
        if value != None:
            self.__Zipcode = value
        return self.__Zipcode

    def Hostname(self, value = None):
        if value != None:
            self.__Hostname = value
        return self.__Hostname
    
    def Timezone(self, value = None):
        if value != None:
            self.__Timezone = value
        return self.__Timezone
    
    def Latitude(self, value = None):
        if value != None:
            self.__Latitude = value
        return self.__Latitude
    
    def Longitude(self, value = None):
        if value != None:
            self.__Longitude = value
        return self.__Longitude
    
    def ASN(self, value = None):
        if value != None:
            self.__ASN = value
        return self.__ASN
    
    def GetColumns(self, value = None):
        return self.__Columns
    
    def AddColumns(self, column:Column = None):
        self.__Columns.append(column)
    
    def ParseFirstByte(self, value:BinaryOption):
        if value.Has(BinaryOption.ISPROXY):
            self.__IsProxy = True
        
        if value.Has(BinaryOption.ISVPN):
            self.__IsVPN = True

        if value.Has(BinaryOption.ISTOR):
            self.__IsTOR = True
        
        if value.Has(BinaryOption.ISCRAWLER):
            self.__IsCrawler = True
        
        if value.Has(BinaryOption.ISBOT):
            self.__IsBot = True
        
        if value.Has(BinaryOption.RECENTABUSE):
            self.__RecentAbuse = True

        if value.Has(BinaryOption.ISBLACKLISTED):
            self.__IsBlackListed = True

        if value.Has(BinaryOption.ISPRIVATE):
            self.__IsPrivate = True
    
    def ParseSecondByte(self, value:BinaryOption):
        if value.Has(BinaryOption.ISMOBILE):
            self.__IsMobile = True

        if value.Has(BinaryOption.HASOPENPORTS):
            self.__HasOpenPorts = True
        
        if value.Has(BinaryOption.ISHOSTINGPROVIDER):
            self.__IsHostingProvider = True
        
        if value.Has(BinaryOption.ACTIVEVPN):
            self.__ActiveVPN = True
        
        if value.Has(BinaryOption.ACTIVETOR):
            self.__ActiveTOR = True

        if value.Has(BinaryOption.PUBLICACCESSPOINT):
            self.__PublicAccessPoint = True
    
    def ConvertConnectionType(self, value:BinaryOption):
        if value.Has(BinaryOption.CONNECTIONTYPETHREE):
            if value.Has(BinaryOption.CONNECTIONTYPETWO):
                return 3
            
            if value.Has(BinaryOption.CONNECTIONTYPEONE):
                return 5
            
            return 1

        if value.Has(BinaryOption.CONNECTIONTYPETWO):
            return 2
        
        if value.Has(BinaryOption.CONNECTIONTYPEONE):
            return 4
        
        return 0
    
    def ConvertAbuseVelocity(self, value:BinaryOption):
        if value.Has(BinaryOption.ABUSEVELOCITYTWO):
            if value.Has(BinaryOption.ABUSEVELOCITYONE):
                return 3
            
            return 1
        
        if value.Has(BinaryOption.ABUSEVELOCITYONE):
            return 2
        
        return 0
    
    def Hostname(self, value:str = None):
        if value != None:
            self.__hostname = value
        return self.__hostname
