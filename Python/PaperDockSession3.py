class Character():
    def __init__(self, NameP, XCoordinateP, YCoordinateP):
        self.__Name = NameP
        self.__XCoordinate = XCoordinateP
        self.__YCoordinate = YCoordinateP
    
    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange
        
Characters = []
try:
    file = open("Character.txt", "r")
    for x in range(10):
        Name = file.readline().strip()
        Xcoord = int(file.readline().strip())
        Ycoord = int(file.readline().strip())
        CharacterObject = Character(Name, Xcoord, Ycoord )
        Characters.append(CharacterObject)
    
except:
    print("file doesnt exists")
    exit()
 
flag = False

while flag == False:
    CharName = input("enter a name ") 
    for x in range(10):
        namefromobject = Characters[x].GetName() 
        if namefromobject.lower() == CharName.lower():
           flag = True
           Position = x 
           
print(Position)        
newflag = False
while newflag == False:
    move = input("Enter a move: ").upper()  # Ensure uppercase input
    if move == "A":
        Characters[Position].ChangePosition(-1, 0)  # Move left
        newflag = True
    elif move == "W":
        Characters[Position].ChangePosition(0, 1)  # Move up
        newflag = True
    elif move == "S":
        Characters[Position].ChangePosition(0, -1)  # Move down
        newflag = True
    elif move == "D":
        Characters[Position].ChangePosition(1, 0)  # Move right
        newflag = True
    else:
        print("Invalid move. Please enter A, W, S, or D.")  # Handle invalid input
    
print(CharName, "has changed to coordinates to X = ", Characters[Position].GetX(), "and Y = " , Characters[Position].GetY())    
