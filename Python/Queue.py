'''
Head is where we are going to insert our data 
Tail is going to be the first free space

           -1   0    1    2    3    4
Names  =      [" ", " ", " ", " "," " ]
         HEAD  TAIL

a queue has two methods:
    Enqueue : add element at the end of the queue if there is an empty space
    Dequeue : Remove element from the start of the queue (if there exists an element)
'''
LenQueue = 5
Names = [""]* LenQueue
HeadPointer = -1
TailPointer = 0
def Enqueue(data):
    global HeadPointer
    global TailPointer
    global Names
    #There should be space in the queue to enqueue smth
    if TailPointer < LenQueue:
        Names[TailPointer] = data
        #For the first insertion, Tail and Head pointers are incremented
        TailPointer += 1
        #HeadPointer should always stay same
        HeadPointer = 0
    else:
        print("Queue is full")


'''
Enqueue
data = Ruth
           -1    0       1    2    3    4
Names  =      ["Ruth ", " ", " ", " "," " ]
         HEAD   TAIL

'''

def DisplayQueue():
    global HeadPointer
    global TailPointer
    global Names
    if HeadPointer == -1:  # Queue is empty
        print("Queue is empty")
    else:
        print("Queue contents:", Names[HeadPointer:TailPointer])


'''
Dequeue

           -1    0       1    2    3    4
Names  =      ["Ruth ", "Sami ", "Meerab ", "Subhan "," " ]
                           HEAD                       TAIL

Second Case: when head and tail are at the same place 
           -1    0       1    2    3    4
Names  =      ["Ruth ", "Sami ", "Meerab ", "Subhan "," " ]
                                                  HEAD|TAIL

'''
def Dequeue():
    global HeadPointer
    global TailPointer
    global Names
    if HeadPointer == -1:
        print("Queue is empty")
    else:
        
        Names[HeadPointer] = ""
        
        HeadPointer += 1
        
    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0

flag = True
while flag:
    inp = input("Enter Command(a to enqueue, b to display,c to dequeue, exit to qui)")
    if inp == "exit":
        flag = False
    elif inp == "a":
        data = input("Please enter data ")
        Enqueue(data)
    elif inp == "b":
        print(Names)
        print("HP: ", HeadPointer)
        print("TP: ", TailPointer)
    elif inp == "c":
        Dequeue()

'''
Enqueue
 


'''