HighScores = []

for i in range(7):
    player_data = ["", "", ""]
    HighScores.append(player_data)
    
def ReadData():
    try:
        file = open("HighScoreTable.txt","r")
        for row in range(7):
            HighScores[row][0] = str(file.readline().strip())  # Player ID
            HighScores[row][1] = str(file.readline().strip())  # Game Level
            HighScores[row][2] = str(file.readline().strip())  # Score
        file.close()  
        return HighScores
    except IOError:
        print("File not found")
        return []
    
def OutputHigScores(Arr):
    for row in range(7):
            PlayerId = Arr[row][0]
            GameLevel = Arr[row][1]
            Score = Arr[row][2]
            print(PlayerId, "reacehd level", GameLevel, " with a score of ", Score)
            
def SortScores(HighScores):
    for x in range(7):
        for y in range(6):
            if int(HighScores[y][1])> int(HighScores[y+1][1]):
                temp = HighScores[y]
                HighScores[y] = HighScores[y+1]
                HighScores[y+1] = temp
    
    for x in range(7):
        for y in range(6):
            if HighScores[y+1][1] == HighScores[y][1]:
                if HighScores[y+1][2]< HighScores[y][2]:
                    temp = HighScores[y]
                    HighScores[y] = HighScores[y+1]
                    HighScores[y+1] = temp
    
    return HighScores

HighScores= ReadData()
print("Before:")
for x in range(7):
    for y in range(3):
        print(HighScores[x][y])
        
OutputHigScores(HighScores)
HighScores = SortScores(HighScores)
print("After:")
for x in range(7):
    for y in range(3):
        print(HighScores[x][y])