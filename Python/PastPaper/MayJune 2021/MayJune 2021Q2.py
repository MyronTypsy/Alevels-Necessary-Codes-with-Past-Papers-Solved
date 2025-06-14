#DECLARE arrayData : ARRAY[0:10] of INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21,8]

def linearSearch(valToFind):
    counter = 0
    while counter <= 10:
        if valToFind == arrayData[counter]:
            return True
        counter += 1
    return False 

valToFind = int(input("Please enter a value to find"))
result = linearSearch(valToFind)
if result == True:
    print("value was found")
else:
    print("not found")