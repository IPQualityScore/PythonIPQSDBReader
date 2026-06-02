class RecordType:
    __data: int = 0

    def __init__(self, data: int | None):
        self.__data = data or 0

    def Has(self, value) -> bool:
        return (self.__data & value)

    def Set(self, value):
        self.__data = self.__data | value

    def ToString(self) -> str:
        if self.Has(RecordType.TREEDATA):
            return "Tree"
        if self.Has(RecordType.STRINGDATA):
            return "String"
        if self.Has(RecordType.SMALLINTDATA):
            return "Small Int"
        if self.Has(RecordType.INTDATA):
            return "Int"
        if self.Has(RecordType.FLOATDATA):
            return "Float"

        return "Unknown"

    def __str__(self) -> str:
        return self.ToString()

    @staticmethod
    def Create(value):
        return RecordType(value)

    # bit one
    IPV4MAP             = 1 << 0
    IPV6MAP             = 1 << 1
    BLACKLISTFILE       = 1 << 2
    RESERVED_SEVEN      = 1 << 3
    RESERVED_EIGHT      = 1 << 4
    RESERVED_NINE       = 1 << 5
    RESERVED_TEN        = 1 << 6
    BINARYDATA          = 1 << 7

    # bit two
    RESERVED_ELEVEN     = 1 << 0
    RESERVED_TWELVE     = 1 << 1
    TREEDATA            = 1 << 2
    STRINGDATA          = 1 << 3
    SMALLINTDATA        = 1 << 4
    INTDATA             = 1 << 5
    FLOATDATA           = 1 << 6
    RESERVED_THIRTEEN   = 1 << 7
