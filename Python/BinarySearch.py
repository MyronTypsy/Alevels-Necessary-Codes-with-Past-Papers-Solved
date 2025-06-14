def BinarySearch(array, target):
    left = 0
    right = len(array) -1
    while left <= 4:
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        elif array[mid]< target:
            left = mid +1
        elif array[mid]> target:
            right = mid -1
    return -1

'''
for a binary search you already have a sorted list and what you have to do is 
you go to the middle check if your target vlue is equal to the mid value then this is the 
best case senario and you return the mid index if not you check if your value is >
or < than the value in the mid position if the target value is less then 
make your right to be mid -1 else vide vera and in the end you return the value

'''