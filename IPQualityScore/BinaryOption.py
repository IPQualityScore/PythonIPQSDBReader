class BinaryOption:
    def __init__(self):
        self.__data = None
    
    def SetData(self, bit):
        self.__data = bit
    
    def Has(self, value):
        return (self.__data & value)
    
    def Set(self, value):
        self.__data = self.__data | value
    
    @staticmethod
    def Create(value):
        result = BinaryOption()
        result.SetData(value)
        return result
    
    IPV4MAP             = 0B0001
    IPV6MAP             = 1 << 1
    TREEDATA            = 1 << 2
    STRINGDATA          = 1 << 3
    SMALLINTDATA        = 1 << 4
    INTDATA             = 1 << 5
    FLOATDATA           = 1 << 6
    BINARYDATA          = 1 << 7
    ISPROXY             = 1 << 0
    ISVPN               = 1 << 1
    ISTOR               = 1 << 2
    ISCRAWLER           = 1 << 3
    ISBOT               = 1 << 4
    RECENTABUSE         = 1 << 5
    ISBLACKLISTED       = 1 << 6
    ISPRIVATE           = 1 << 7
    ISMOBILE            = 1 << 0
    HASOPENPORTS        = 1 << 1
    ISHOSTINGPROVIDER   = 1 << 2
    ACTIVEVPN           = 1 << 3
    ACTIVETOR           = 1 << 4
    PUBLICACCESSPOINT   = 1 << 5
    RESERVEDONE         = 1 << 6
    RESERVEDTWO         = 1 << 7
    RESERVEDTHREE       = 1 << 0
    RESERVEDFOUR        = 1 << 1
    RESERVEDFIVE        = 1 << 2
    CONNECTIONTYPEONE   = 1 << 3
    CONNECTIONTYPETWO   = 1 << 4
    CONNECTIONTYPETHREE = 1 << 5
    ABUSEVELOCITYONE    = 1 << 6
    ABUSEVELOCITYTWO    = 1 << 7