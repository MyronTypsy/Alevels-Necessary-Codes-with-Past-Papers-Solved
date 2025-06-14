#DECLARE SaleData : Record
class SaleData():
    def __init__(self, IDP,QuantityP):
        self.ID = IDP
        self.Quantity = QuantityP
        
#DECLARE CircularQueue : Array[0:5] of SaleData
#DECLARE HeadPointer: INTEGER
#DECLARE TailPointer: INTEGER

global CircularQueue
global HeadPointer
global TailPointer
CircularQueue = []
HeadPointer= 0
TailPointer= 0
NumberOfItems =0
for x in range(0, 5):
    CircularQueue.append((SaleData("",-1)))
 
for x in range(0,5):
    IDI= SaleData.ID = " "
    QUAN = SaleData.Quantity = -1

def Enqueue(NewRecord):
    global NumberOfItems
    global CircularQueue
    global HeadPointer
    global TailPointer
    CircularQueue[TailPointer]= (IDI,str(QUAN))
    if TailPointer ==5 :    
        return -1
    else:
        CircularQueue[TailPointer] = NewRecord
        if(Tail == 4):
            Tail = 0
        else:
            Tail +=1
            NumberOfItems +=1
        return 1

def Dequeue():
    global NumberOfItems
    global CircularQueue
    global HeadPointer
    global TailPointer
    if NumberOfItems == 0:
        EmptyRec = print(" ", -1)  
        return EmptyRec
    else:
        Rec= CircularQueue[HeadPointer]
        NumberOfItems -=1
        return Rec
    
def EnterRecord(): 
    ID = input("Enter Id")
    Quantity = input("Enter Quantity")
    record = SaleData(ID,Quantity)
    if Enqueue(record) == -1:
        print("Full")
    else:
        print("stored")
         
EnterRecord()
EnterRecord() 
EnterRecord() 
EnterRecord() 
EnterRecord() 
EnterRecord() 

'''RecordCheck = Dequeue()
if RecordCheck.SaleData.ID == " ":
    print("Queue is full")
else:
    '''