def ReadData():
    array = []
    try:
        file = open("Data.txt","r")
        for count in range(45):
            data = file.readline().strip()
            array.append(data)
            array[count] = data
        file.close()
        return array
    except IOError:
        print("file not found")
    


def FormatArray(DataArray):
    OutputText = ""
    for count in range(0,45):
        OutputText = OutputText + DataArray[count] + " "
    return OutputText


data= ReadData()
print(FormatArray(data))

def CompareStrings(Str1, Str2):
    count = 0
    while True:
        if Str1[count] < Str2[count]:
            return 1
        elif Str1[count] > Str2[count]:
            return 2
        else:
            count += 1