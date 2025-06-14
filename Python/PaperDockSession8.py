import datetime
todaydate = datetime.datetime(2024, 1, 1)
class Character:
    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP):
        #PRIVATE CharacterName : STRING
        #PRIVATE DateOfBirth : DATE
        #PRIVATE Intellignence : REAL
        #PRIVATE speed : INTEGER

        self.__CharacterName = CharacterNameP
        self.__DateOfBirth = DateOfBirthP
        self.__Intelligence = IntelligenceP
        self.__Speed = SpeedP
    
    def GetIntelligence(self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    def SetIntelligence(self, NewIntelligence):
        self.__Intelligence = NewIntelligence
        
    def Learn(self):
        
        Increase = self.__Intelligence * (10/100)
        self.__Intelligence = self.__Intelligence + Increase
    
    def  ReturnAge(self):
        Age = 2024 - self.__DateOfBirth.year
        return Age
    
FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30 )
FirstCharacter.Learn()
print(FirstCharacter.GetName(), "is", FirstCharacter.ReturnAge(), "years old and has intelligence", FirstCharacter.GetIntelligence())

class MagicCharacter(Character):
    #PRIVATE Element: STRING
    def __init__(self,  CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP, ElementP):
        super().__init__(CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP)
        self.__Element = ElementP
        
    def Learn(self):
        current_intelligence = super().GetIntelligence()
        if (self.__Element == "fire"  or self.__Element == "water"):
            super().SetIntelligence(current_intelligence + (current_intelligence * 20/100 ))
        elif (self.__Element == "earth"):
            super().SetIntelligence(current_intelligence + (current_intelligence * 30/100 ))
        else: 
            super().SetIntelligence(current_intelligence + (current_intelligence * 10/100 ))

        
FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3,3), 75, 22, "fire")

FirstMagic.Learn()
print(FirstMagic.GetName(), "is", FirstMagic.ReturnAge(), "years old and has intelligence", FirstMagic.GetIntelligence())
