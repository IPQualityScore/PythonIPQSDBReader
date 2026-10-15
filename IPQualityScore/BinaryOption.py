class BinaryOption:
    __data: int

    def __init__(self):
        self.__data = 0

    def SetData(self, bit: int):
        self.__data = bit or 0

    def Has(self, value: int) -> bool:
        return (self.__data & value) != 0

    def Set(self, value: int):
        self.__data = self.__data | value

    @staticmethod
    def Create(value: int | None):
        result = BinaryOption()
        if value is not None:
            result.SetData(value)
        return result

	# reserved bit one
    ISPROXY             = 1 << 0
    ISVPN               = 1 << 1
    ISTOR               = 1 << 2
    ISCRAWLER           = 1 << 3
    ISBOT               = 1 << 4
    RECENTABUSE         = 1 << 5
    ISBLACKLISTED       = 1 << 6
    ISPRIVATE           = 1 << 7

	# reserved bit two
    ISMOBILE            = 1 << 0
    HASOPENPORTS        = 1 << 1
    ISHOSTINGPROVIDER   = 1 << 2
    ACTIVEVPN           = 1 << 3
    ACTIVETOR           = 1 << 4
    PUBLICACCESSPOINT   = 1 << 5
    FREQUENTABUSER      = 1 << 6
    TRUSTEDAPPLICATION  = 1 << 7

	# reserved bit three
    SHARED_IP           = 1 << 0
    SECYRUTYSCANNER     = 1 << 1
    DYNAMIC_IP          = 1 << 2
    CONNECTIONTYPEONE   = 1 << 3
    CONNECTIONTYPETWO   = 1 << 4
    CONNECTIONTYPETHREE = 1 << 5
    ABUSEVELOCITYONE    = 1 << 6
    ABUSEVELOCITYTWO    = 1 << 7
