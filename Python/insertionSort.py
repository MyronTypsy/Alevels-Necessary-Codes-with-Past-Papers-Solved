'''
three things to remember 
there is always going to be i, j and a key that stores the current value
then 
       0  1  2  3  4  5  6   7    8
arr = [5, 9, 6, 3, 7, 2, 99, 420, 53]
       j  i 
always start from 1 and scheck the previous value (j =i -1)
now compare the key value with arr[j]
if both conditions are true then swap j value to j + 1
now decrement j and if j is less than 0 then only come out of the loop and give key its original value
else at the place assign key value to arr[j+1]

'''


def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key    

arr = [5, 9, 6, 3, 7, 2, 99, 420, 53]
InsertionSort(arr) 
print(arr)    
    
#practice code

'''def InsertionSort(arr):
    for i in range(1, len(arr)):
        itemSelected = arr[i]
        j =i -1
        while j>0 and itemSelected > arr[j]:
            arr[j+1]= arr[j]
            j-=1
        arr[j+1]= itemSelected'''
        
