data =[]*45
def ReadData():
    try:
        file = open("Data.txt", "r")
        for x in range(45):
            data.append(file.readline().strip("\n"))
        file.close()
        
        return data
    except IOError():
        print("file not found")

'''out = ReadData()
print(out)'''

def ForamtArray(array):
    output = ""
   
    for x in range(45):
        element = array[x]
        output = output +  element + " "
    return output

out = ReadData()
print(out)
out2= ForamtArray(data)
print(out2)

def ComareStrings(str1, str2):
    flag = False
    x = 0 
    while flag == False:
        
            if str1[x] > str2[x]:
                flag = True
                return 2
            elif str1[x] < str2[x]:
                flag = True
                return 1
            else : # str1[0] = str2[0]:
                flag2 = True
                while flag2 == True:
                    x = x+1
                    if str1[x] > str2[x]:
                        flag = False
                        return 2
                    elif str1[x] < str2[x]:
                        flag = False
                        return 1                  


'''
Checks is code runs properly
print(ComareStrings("ruth", "fatima"))'''

def Bubble(arr):
    
    for x in range(0, len(arr)):
        for y in range(0, len(arr) -1):
            if ComareStrings(arr[y], arr[y+1]) == 2:
                temp = arr[y+1]
                arr[y+1] = arr[y]
                arr[y] = temp
                
    return arr

Bubble(data)
print(ForamtArray(data))

    