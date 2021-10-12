from IPQualityScore.BinaryOption import BinaryOption

class Column:

    def __init__(self):
        self.__Name     = None
        self.__RawValue = None
        self.__Type     = None
        self.__Name     = None
        self.__Value    = None

    @staticmethod
    def Create(name, stype, value= None):
        C = Column()
        C.Name(name)
        C.Type(stype)
        C.Value(value)

        return C
    
    def Name(self, value = None):
        if value != None:
            self.__Name = value
        return self.__Name

    def Type(self, value:BinaryOption = None):
        if value != None:
            self.__Type  = value
        return self.__Type
    
    def Value(self, value = None):
        if value != None:
            self.__Value = value
        return self.__Value