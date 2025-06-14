'''
Question
Sorting

#DECLARE Animal : ARRAY [0:9] OF STRING
Animals = []
Animals.append("horses")
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
    ArrayLength = len(Animals)
    for x in range(0, ArrayLength -1):
        for y in range(0, ArrayLength- x -1):
            if Animals[y][0] < Animals[y +1][0]:
                Temp = Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1] = Temp
                 
SortDescending()
for index in range(0, 9):
    print(Animals[index])
    
'''

#DECLARE DataArray : ARRAY [0:24] OF INTEGER

DataArray =[]
try:
    file = open("Data.txt", "r") 
    for z in range(0, 24):
        filedata = int(file.readline().strip())
        DataArray.append(filedata)
    file.close()
except IOError:
    print("File doesnt exist")
    
def PrintArray(int):
    FinalString = ""
    for j in range(25):
        FinalString = FinalString + int[j] +" "
        
def LinearSearch(Arr, SearchVal):
    for a in range( len(Arr)):
        if SearchVal == Arr[a]:
            SearchValue += SearchVal
    print("The number ", SearchVal, "is found ", SearchValue, "times"   ) 
 

Num = int(input("Enter a num between 0 and 100: "))

while Num < 0 or Num > 100:

    print("Invalid Input Enter Again")
    input = Num

LinearSearch(DataArray, 5)
