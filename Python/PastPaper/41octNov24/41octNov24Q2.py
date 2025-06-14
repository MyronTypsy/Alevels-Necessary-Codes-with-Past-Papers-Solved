class Horse():
    #PRIVATE Name : String
    #PRIVATE MaxFenceHeight : Integer
    #PRIVATE PercentageSuccess : Integer
    def __init__(self, NameP, MaxFenceHeightP, PercentageSuccessP):
        self.__Name = NameP
        self.__MaxFenceHeight = MaxFenceHeightP
        self.__PercentageSuccess = PercentageSuccessP

    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success(self, Height, Risk):
        Values = [[5, 0.6], [4,0.7],[3,0.8],[2,0.9],[1,1]]
        if Height > self.__MaxFenceHeight:
            return (self.__PercentageSuccess*0.2)
        elif Height <=  self.__MaxFenceHeight:
            for x in range(5):
                if Risk == Values[x][0]:
                    Chance = Values[x][1] * self.__PercentageSuccess
        return Chance
    
#DECLARE Horses : Array[0:2] of Horse
Horses = []
Horsy1= Horse("Beauty", 150, 72)
Horsy2 = Horse("Jet", 160, 65)
Horses.append(Horsy1)
Horses.append(Horsy2)

for x in range(2):
    print(Horses[x].GetName())
    
class Fence():
    #PRIVATE Height : Integer
    #PRIVATE Risk : Integer 
    def __init__(self, HeightP, RiskP):
        self.__Height = HeightP
        self.__Risk = RiskP
    
    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk
    
Course = []*4
for x in range(4):
    Height = int(input("Enter Height"))
    while Height < 70 or Height > 180:
        print("Height should be only between 70 and 180 inclusive")
        Height = int(input("Enter Height"))
    Risk = int(input("Enter Risk"))
    while Risk < 1 or Risk > 5:
        print("Height should be only between 1 and 5 inclusive")
        Risk = int(input("Enter Risk"))
    Course.append(Fence(Height, Risk))

for y in range(0, 2):
    for x in range(0, 4):
        Chances = Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
        print(Horses[y].GetName(), "Fence", x + 1, "chance of success is", Chances, "%")

AverageSuccess = []
for y in range(0,2):
    Total = 0
    for x in range(0,4):
        Chances = Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
        print(Horses[y].GetName(), "Fence", x + 1, "chance of success is", Chances, "%")
        Total = Total + Chances
    Average = Total/4
    AverageSuccess.append(Average)
    print(Horses[y].GetName(),"average success rate is", Average, "%")
    
Highest = AverageSuccess[0]
Winner = -1
for x in range(1,2):
    if Highest < AverageSuccess[x]:
        Winner= x
        Highest = AverageSuccess[x]
print(Horses[Winner].GetName(), " has the highest average chance of success ")