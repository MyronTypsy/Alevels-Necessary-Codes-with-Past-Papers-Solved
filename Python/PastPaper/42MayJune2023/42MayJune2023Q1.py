#DECLARE Animal OF Array[0:10] AS STRING
global Animals
Animals = []
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDescending():
    #DECLARE ArrayLength : INTEGER
    #DECLARE Temp : STRING
    ArrayLength = 10
    for x in range(0,ArrayLength-1):
        for y in range(0,ArrayLength-x-1):
            if Animals[y][0]< Animals[y+1][0]:
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1]= temp
    
SortDescending()
for z in range(0, 10):    
    print(Animals[z])
