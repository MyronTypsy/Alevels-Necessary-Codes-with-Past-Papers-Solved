class Character:
    def __init__(self,  XPositionP, YPositionP, NameP):
        #DECLARE Public Name : STRING
        #DECLARE Public XPosition : INTEGER
        #DECLARE Public YPosition : INTEGER
        
        self.__XPosition = XPositionP
        self.__YPosition = YPositionP
        self.__Name = NameP
        
        def GetXPosition(self):
            return self.__XPosition
        def GetYPosition(self):
            return self.__YPosition
        
        def SetXPosition(self, vX):
            self.__XPosition += vX
            if self.__XPosition > 10000:
                self.__XPosition = 1000
            if self.__XPosition < 0:
                self.__XPosition = 0
            
        def SetYPosition(self, vY):
            self.__YPosition += vY
            if self.__YPosition > 10000:
                self.__YPosition = 1000
            if self.__YPosition < 0:
                self.__YPosition = 0
                
        def Move(self, Direction):
            if (Direction == "up"):
                self.SetYPosition(10)
            elif (Direction == "down"):
                self.SetYPosition(-10)
            elif(Direction == "right"):
                self.SetXPosition(10)
            else:
                self.SetXPosition(-10)
                                
Jack = Character( 50, 50, "Jack")

class BikeCharacter(Character):
    def __init__(self, XPositionP, YPositionP, NameP):
        super().__init__(XPositionP, YPositionP, NameP)
        def Move(self, Direction):
            if (Direction == "up"):
                super().SetYPosition(20)
            elif (Direction == "down"):
                super().SetYPosition(-20)
            elif(Direction == "right"):
                super().SetXPosition(20)
            else:
                super().SetXPosition(-20)
                
Karla = BikeCharacter(100,50, "Karal")

CharacterToMove = input("Enter a character youd like to move: ").lower()
while CharacterToMove != "jack" and CharacterToMove != "karla":
    CharacterToMove = input("Invalid try again")
Direction = input("Which direction? Up, down, left or right?").lower()
while Direction != "up" and Direction != "down" and Direction != "left" and Direction !="right":
    Direction = input("Invalid try again").lower() 
if CharacterToMove == "jack":
    Jack.Move(Direction)
    print("Jack's new position is X =", Jack.GetXPosition(), "Y =", Jack.GetYPosition())
else:
    Karla.Move(Direction)
    print("Karla's new position is X =", Karla.GetXPosition(), "Y =", Karla.GetYPosition())

