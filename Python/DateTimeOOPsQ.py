import datetime
class Character():
    def __init__(self, CharacterNameP, DateOfBirthP, Intelligence, SpeedP):
        self.__CharacterName = CharacterNameP
        self.__DateOfBirth = DateOfBirthP
        self.__Intelligence = Intelligence
        self.__Speed = SpeedP
        
    def SetIntelligence(self, intelligence):
            self.__Intelligence = intelligence
        
    def GetIntelligence(self):
            return self.__Intelligence
        
    def GetName(self):
            return self.__CharacterName       
        
    def Learn(self):
            self.__Intelligence = self.__Intelligence + (self.__Intelligence *0.1)
            
    def ReturnAge(self):
            DOB  = self.__DateOfBirth.year
            
            Age = 2023 - DOB
            return Age

FirstCharacter = Character("Royal", datetime.datetime(2019,1,1), 70.0, 30)
FirstCharacter.Learn()
print(FirstCharacter.GetName(), "is", FirstCharacter.ReturnAge(), "years old and is intelligence is ", FirstCharacter.GetIntelligence())

class MagicCharacter(Character):
    def __init__(self, CharacterNameP, DateOfBirthP, Intelligence, SpeedP, ElementP):
           super().__init__( CharacterNameP, DateOfBirthP, Intelligence, SpeedP)
           self.__Element = ElementP
    
    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            newIntelligence = super().GetIntelligence() + (super().GetIntelligence() * 0.2)
        elif self.__Element == "earth":
            newIntelligence = super().GetIntelligence() + (super().GetInteligence()*0.3)
        else:
            newIntelligence = super().GetIntelligence()+(super().GetIntelligence() * 0.1)
            
        super().SetIntelligence(newIntelligence)

FirstMagic = MagicCharacter("Light", datetime.datetime(2018,3,3), 75,22, "fire")
FirstMagic.Learn()
print(FirstMagic.GetName(),"is ", FirstMagic.ReturnAge(), "years old and is intelligence is ", FirstMagic.GetIntelligence()  )