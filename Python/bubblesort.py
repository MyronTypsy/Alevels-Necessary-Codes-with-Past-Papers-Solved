arr = [5, 9, 6, 3, 7, 2, 99, 420, 53]

def swap(a,b):
    temp = a
    a= b
    b = temp
    return a, b

def BubbleSort(arr):
    boundary = len(arr)-1 
    check = False
    while check == False:
        check = True
        for i in range(boundary):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = swap(arr[i], arr[i+1])
                check = False

BubbleSort(arr)
print("Sorted Array:", arr)

