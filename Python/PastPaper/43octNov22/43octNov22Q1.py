#DECLARE DataArray as Array[0:100] of INTEGER
global DataArray
DataArray = [0 for I in range (100)]

def ReadFile():
    global DataArray
    
    try:
        file = open("IntegerData.txt","r")
        for x in range(100):
            data = file.readline().strip()
            DataArray[x]= int(data)
        file.close()
    except IOError:
        print("File not found")
        
def FindValue():
    count = 0
    global DataArray
    flag= True
    while flag == True:
        num = int(input("Enter a number from 0 to 100 inclusive "))
        if num <0 or num >100:
            flag = True
        else:
            flag = False
    
    for x in range(100):
        if DataArray[x] == num:
            count +=1
    
    return count 

ReadFile()
found = FindValue()
print("the input number has been found " , found, "times")

def BubbleSort():
    global DataArray
    for x in range(0,99):
        for y in range(0,98):
            if DataArray[y]> DataArray[y+1]:
                temp =DataArray[y]
                DataArray[y]= DataArray[y+1]
                DataArray[y+1]= temp
                
ReadFile() 
print("the input number has been found " , found, "times")

BubbleSort() 
print(DataArray)