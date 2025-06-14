#Basically a class all the attributes are public
#Following is how to make a record and quetion solved is from 9618/42/M/J/2
class SaleData():
    def __init__(self, IdP, QuantP):
        self.Id = IdP
        self.Quant = QuantP


global CircularQueue
global Head
global Tail
global NumberOfItems
NumberOfItems = 0
Head = 0
Tail = 0
#DECLARE CircularQueue :ARRAy[0:4}] OG SaleData
CircularQueue = [SaleData("", -1) for _ in range(5)]

def Enqueue(RecordOfData):
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = RecordOfData
        if Tail == 4:
            Tail = 0
        else: 
            Tail += 1
        NumberOfItems += 1
        return 1
    
def Dequeue():
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    if NumberOfItems ==0:
        return SaleData(" " , -1)
    else:
        record = CircularQueue[Head]
        Head = (Head + 1) 
        if Head > 4:
            Head = 0
        NumberOfItems = NumberOfItems -1
        return record
    
def EnterRecord():
    ID = input("Enter the sale id : ")
    Quantity =  int(input("Enter the sale quantity : "))
    NewRecord = SaleData(ID, Quantity)
    result = Enqueue(NewRecord)
    if result == -1:
        print("Full")
    else:
        print("Stored")

EnterRecord()  
EnterRecord()  
EnterRecord()  
EnterRecord()  
EnterRecord()  
EnterRecord()  

discard = Dequeue()
if discard.Id == " ":
    print("queue is empty")
else:
    print(discard.Id, " ", str(discard.Quant))
    
EnterRecord()
for x in range(5):
    Record = CircularQueue[x]
    print(Record.Id, " ", str(Record.Quant) )