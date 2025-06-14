class Vehicle():
        #PRIVATE ID : STRING
        #PRIVATE MaxSpeed : INTEGER
        #PRIVATE CurrentSpeed : INTEGER
        #PRIVATE IncreaseAmount : INTEGER
        #PRIVATE HorizontalPosition : INTEGER
    def __init__(self, IDP, MaxSpeedP, CurrentSpeedP, IncreaseAmountP, HorizontalPositionP):
        self.__Id = IDP
        self.__MaxSpeed = MaxSpeedP
        self.__CurrentSpeed = CurrentSpeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__HorizontalPosition = HorizontalPositionP
        
    def    GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.____IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.____HorizontalPosition
    
    def MaxSpeed(self):
        return self.____MaxSpeed
    
    def SetCurrentSpeed(self, NewCurrentSpeed):
        self.__CurrentSpeed = NewCurrentSpeed
     
    def SetCurrentSpeed(self, NewHorizontalPosition):
        self.__HorizontalPosition = NewHorizontalPosition   
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
            
        self.__HorizontalPosition = self.__CurrentSpeed + self.__HorizontalPosition
    
    def Output(self):
        print("Current Speed: ", self.__CurrentSpeed)
        print("Horizontal Position ", self.__HorizontalPosition)
        
class Helicopter(Vehicle):
    #PRIVATE VerticlePosition : INTEGER
    #PRIVATE VerticleChange : INTEGER
    #PRIVATE MaxHeight : INTEGER
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VerticleChangeP, MaxHeightP  ):
        
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticleChange = VerticleChangeP
        self.__MaxHeight = MaxHeightP
        self.__VerticlePosition = 0
        
    def IncreaseSpeed(self):
        self.__VerticlePosition = self.__VerticlePosition + self.__VerticleChange
        if self.__VerticlePosition > self.__MaxHeight:
            self.__VerticlePosition = self.__MaxHeight
        super().IncreaseSpeed()
    
    def Output(self):
        super().Output()
        print("Current Verticle Position: ", self.__VerticlePosition)
    
    