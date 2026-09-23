from IPQualityScore.BinaryOption    import BinaryOption
from IPQualityScore.Columns         import Column

class IPQSRecord:
    def __init__(self):
        self.__IsProxy            = False
        self.__IsVPN              = False
        self.__IsTOR              = False
        self.__IsCrawler          = False
        self.__IsBot              = False
        self.__RecentAbuse        = False
        self.__IsBlackListed      = False
        self.__IsPrivate          = False
        self.__IsMobile           = False
        self.__HasOpenPorts       = False
        self.__IsHostingProvider  = False
        self.__ActiveVPN          = False
        self.__ActiveTOR          = False
        self.__PublicAccessPoint  = False
        self.__FrequentAbuser     = False
        self.__TrustedApplication = False
        self.__SecurityScanner    = False
        self.__SharedIP           = False
        self.__DynamicIP          = False

        self.__ConnectionTypeRaw = 0
        self.__AbuseVelocityRaw  = 0

        self.__Country           = ""
        self.__City              = ""
        self.__Region            = ""
        self.__ISP               = ""
        self.__Organization      = ""
        self.__Zipcode           = ""
        self.__Hostname          = ""
        self.__ASN               = 0
        self.__Timezone          = ""
        self.__Latitude          = 0.0
        self.__Longitude         = 0.0

        self.__FraudScore: dict[int, int] = {}
        self.__Columns: list[Column] = []

    def IsProxy(self, value: bool|None = None) -> bool:
        if value is not None:
           self.__IsProxy = value
        return self.__IsProxy

    def IsVPN(self, value: bool|None = None) -> bool:
        if value is not None:
           self.__IsVPN = value
        return self.__IsVPN

    def IsTOR(self, value: bool|None = None) -> bool:
        if value is not None:
           self.__IsTOR = value
        return self.__IsTOR

    def IsCrawler(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__IsCrawler = value
        return self.__IsCrawler

    def IsBot(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__IsBot = value
        return self.__IsBot

    def RecentAbuse(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__RecentAbuse = value
        return self.__RecentAbuse

    def IsBlackListed(self, value: bool|None = None):
        if value is not None:
            self.__IsBlackListed = value
        return self.__IsBlackListed

    def IsPrivate(self, value: bool|None = None):
        if value is not None:
            self.__IsPrivate = value
        return self.__IsPrivate

    def IsMobile(self, value: bool|None = None):
        if value is not None:
            self.__IsMobile = value
        return self.__IsMobile

    def HasOpenPorts(self, value: bool|None = None):
        if value is not None:
            self.__HasOpenPorts = value
        return self.__HasOpenPorts

    def IsHostingProvider(self, value: bool|None = None):
        if value is not None:
            self.__IsHostingProvider = value
        return self.__IsHostingProvider

    def ActiveVPN(self, value: bool|None = None):
        if value is not None:
            self.__ActiveVPN = value
        return self.__ActiveVPN

    def ActiveTOR(self, value: bool|None = None):
        if value is not None:
            self.__ActiveTOR = value
        return self.__ActiveTOR

    def PublicAccessPoint(self, value: bool|None = None):
        if value is not None:
            self.__PublicAccessPoint = value
        return self.__PublicAccessPoint

    def FrequentAbuser(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__FrequentAbuser = value
        return self.__FrequentAbuser

    def TrustedApplication(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__TrustedApplication = value
        return self.__TrustedApplication

    def SecurityScanner(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__SecurityScanner = value
        return self.__SecurityScanner

    def SharedIP(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__SharedIP = value
        return self.__SharedIP

    def DynamicIP(self, value: bool|None = None) -> bool:
        if value is not None:
            self.__DynamicIP = value
        return self.__DynamicIP

    def ConnectionTypeRaw(self, value:BinaryOption|None = None) -> int:
        if value is not None:
            self.__ConnectionTypeRaw = self.ConvertConnectionType(value)
        return self.__ConnectionTypeRaw

    def ConnectionType(self, value:BinaryOption|None = None) -> str:
        if value is not None:
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

    def FraudScore(self, strictness:int = 0, value:int|None = None) -> int:
        if value is not None:
            self.__FraudScore[strictness] = value
        return self.__FraudScore[strictness]

    def SetFraudScore(self,strictness:int, value:int):
        self.__FraudScore[strictness] = value

    def AbuseVelocityRaw(self, value:BinaryOption|None = None) -> int:
        if value is not None:
            self.__AbuseVelocityRaw = self.ConvertAbuseVelocity(value)
        return self.__AbuseVelocityRaw

    def AbuseVelocity(self, value:BinaryOption|None = None) -> str:
        if value is not None:
            self.__AbuseVelocityRaw = self.ConvertAbuseVelocity(value)
        items = {
            1: "low",
            2: "medium",
            3: "high",
        }
        if self.__AbuseVelocityRaw in items:
            return items[self.__AbuseVelocityRaw]
        else:
            return "none"

    def Country(self, value:str|None = None) -> str:
        if value is not None:
            self.__Country = value
        return self.__Country

    def City(self, value:str|None = None) -> str:
        if value is not None:
            self.__City = value
        return self.__City

    def Region(self, value:str|None = None) -> str:
        if value is not None:
            self.__Region = value
        return self.__Region

    def ISP(self, value:str|None = None) -> str:
        if value is not None:
            self.__ISP = value
        return self.__ISP

    def Organization(self, value:str|None = None) -> str:
        if value is not None:
            self.__Organization = value
        return self.__Organization

    def Zipcode(self, value:str | None = None):
        if value is not None:
            self.__Zipcode = value
        return self.__Zipcode

    def Hostname(self, value:str | None = None):
        if value is not None:
            self.__Hostname = value
        return self.__Hostname

    def ASN(self, value:int|None = None) -> int:
        if value is not None:
            self.__ASN = value
        return self.__ASN

    def Timezone(self, value:str|None = None) -> str:
        if value is not None:
            self.__Timezone = value
        return self.__Timezone

    def Latitude(self, value:float|None = None) -> float:
        if value is not None:
            self.__Latitude = value
        return self.__Latitude

    def Longitude(self, value:float|None = None) -> float:
        if value is not None:
            self.__Longitude = value
        return self.__Longitude

    def GetColumns(self) -> list[Column]:
        return self.__Columns

    def AddColumns(self, column:Column | None = None):
        if column is not None:
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

        if value.Has(BinaryOption.FREQUENTABUSER):
            self.__FrequentAbuser = True

        if value.Has(BinaryOption.TRUSTEDAPPLICATION):
            self.__TrustedApplication = True

    def ParseThirdByte(self, value:BinaryOption):
        if value.Has(BinaryOption.SHARED_IP):
            self.__SharedIP = True

        if value.Has(BinaryOption.SECYRUTYSCANNER):
            self.__SecurityScanner = True

        if value.Has(BinaryOption.DYNAMIC_IP):
            self.__DynamicIP = True

    def ConvertConnectionType(self, value: BinaryOption) -> int:
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

    def ConvertAbuseVelocity(self, value:BinaryOption) -> int:
        if value.Has(BinaryOption.ABUSEVELOCITYTWO):
            if value.Has(BinaryOption.ABUSEVELOCITYONE):
                return 3

            return 1

        if value.Has(BinaryOption.ABUSEVELOCITYONE):
            return 2

        return 0
