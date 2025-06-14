global Queue
global HeadPointer
global TailPointer
Queue = [] # ARRAY [0:50] of STRING
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer == 50:
        print("queue is full")
    else:
        Queue.append(Data)
        TailPointer +=1
        if HeadPointer == -1:
            HeadPointer = 0
            
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("queue is empty")
        return "Empty"
    else:
        HeadPointer +=1
        return Queue[HeadPointer -1]
        
def ReadData():
    try:
        ID = open("QueueData.txt", "r")
        for line in ID:
            Enqueue(line.strip())
        ID.close()
    except IOError:
        print("File doesnt exists")
        
class RecordData():
    #DECLARE PUBLIC ID: STRING
    #DECLARE PUBLIC Total: INTEGER
    def __init__(self, IDp, TotalP):
        self._ID = IDp
        self._Total = TotalP
    
    def GetID(self):
        return self._ID
    
    def GetTotal(self):
        return self._Total

    def SetTotal(self, Value):
        self._Total = Value
        
    def SetID(self, Value):
        self._ID = Value

global Records
global NumberRecords
Records = [] #50 items
NumberRecords = 0

def TotalData():
    global NumberRecords
    #DECLARE DataAccessed :STRING
    #DECLARE Flag : BOOLEAN
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0 :
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1
        Flag = True
    else:
        for X in range(0, NumberRecords):
            if Records[X].GetID() == DataAccessed:
                Records[X].SetTotal(Records[X].GetTotal()+1) 
                Flag = True
        if Flag == False:
            Records.append(RecordData(DataAccessed,  1))
            NumberRecords+=1

def OutputRecords():
    for X in range(0, NumberRecords):
        print("ID", Records[X].GetID(), " Total ", Records[X].GetTotal())
        
ReadData()
TotalData()
OutputRecords()