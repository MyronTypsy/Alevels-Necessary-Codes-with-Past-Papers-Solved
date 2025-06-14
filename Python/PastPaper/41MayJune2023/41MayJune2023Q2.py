class Vehicle():
    def __init__(self, IDP,MaxSpeedP,IncreaseAmountP):
        self.__ID = IDP
        self.__MaxSpeed =MaxSpeedP
        self.__CurrentSpeed = 0
        self.__IncreaseAmount =IncreaseAmountP
        self.__HorizontalPosition = 0
        
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed =CSP
        
    def SetHorizontalPosition(self,HP):
        self.__HorizontalPosition =HP
        
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed
        
    def OutputValues(self):
        HorizontalPosition = print("Horizontal Position is ", self.__HorizontalPosition)
        Speed = print("Speed of the Vehicle is ", self.__CurrentSpeed)

class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP,VerticalChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChangeP
        self.__MaxHeight = MaxHeightP
    
    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()
        
    def OutputtedValues(self):
        VeticalPosition = print("Vertical Position is ", self.__VerticalPosition)
        super().OutputValues()
        
Car = Vehicle("Tiger", 100, 20)
Heli = Helicopter("Lion", 350,40,3,100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputValues()

Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
Heli.OutputtedValues()

    
        