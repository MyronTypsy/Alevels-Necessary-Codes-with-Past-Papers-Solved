class Horse:
    def __init__(self, NameP, MaxFenceHeightP, PercentageSuccessP):
        self.__Name = NameP
        self.__MaxFenceHeight = MaxFenceHeightP
        self.__PercentageSuccess = PercentageSuccessP
        
        def GetName(self):
            return self.__Name
        
        def GetMaxFenceHeight(self):
            return self.__MaxFenceHeight
        Horses =[]
        Horses.append(Horse("Beauty", 150, 72))
        Horses.append(Horse("Jet", 160, 65))
        print(Horses[0].GetName())
        print(Horses[1].GetName())
