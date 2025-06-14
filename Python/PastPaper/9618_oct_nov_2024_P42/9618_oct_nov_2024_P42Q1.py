class EventName():
    #DECLARE EventName : STRING
    #DECLARE Type : STRING
    #DECLARE Difficulty : INTEGER
    def __init__(self, EventNameP, TypeP, DifficultyP):
        self.__EventName = EventNameP
        self.__Type = TypeP
        self.__Difficulty = DifficultyP
            
    def GetName(self):
        return self.__EventName
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetEventType(self):
        return self.__Type

#DECLARE Group[0:4] OF EventItem
Group = []


Group.append(EventName("Bridge","jump",3))
Group.append(EventName("Water wade","swim",4))
Group.append(EventName("100 mile run","run",5))
Group.append(EventName("Gridlock","drive",2))
Group.append(EventName("Wall on wall","jump",4))

class Character():
    #DECLARE CharacterName : STRING
    #DECLARE Jump : INTEGER
    #DECLARE Swim : INTEGER
    #DECLARE Run : INTEGER
    #DECLARE Drive : INTEGER
    
    def __init__(self, CharsacterNameP, JumpP, SwimP, RunP, DriveP):
        self.__CharacterName = CharsacterNameP
        self.__Jump = JumpP
        self.__Swim = SwimP
        self.__Run = RunP
        self.__Drive = DriveP
        
    def GetName(self):
        return self.__CharacterName
    
    def CalculateScore(self, Type, Difficulty):
        if Type == "jump":
            Chance = self.__Jump
        elif Type == "swim":
            Chance = self.__Swim
        elif Type == "run":
            Chance = self.__Run
        else:
            Chance = self.__Drive
        if Chance >= Difficulty:
            return 100
        else:
            Difference = Difficulty - Chance
            if Difference == 1:
                return 80
            elif Difference == 2:
                return 60
            elif Difference == 3:
                return 40
            elif Difference == 4:
                return 20
            else:
                return 0
        
P1 = Character("Tarz", 5, 3, 5, 1)
P2 = Character("Geni", 2, 2, 3, 4)
P1Points = 0
P2Points = 0

for x in range(5):
    P1EventScores = P1.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
    P2EventScores = P2.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
    
    if P1EventScores == P2EventScores:
        print("its a draw")
    elif P1EventScores > P2EventScores:
        P1Points += 1
        print("Tarz won this event")
    else:
        P2Points += 1
        print("Geni has won the event")
        
if P1Points> P2Points:
    print("Tarz has won this group")
else:
    print("Geni has won this group")