QueueArray = []*100
global Headpointer
global TailPointer

class Queue():
    def __init__(self, HeadPointerP, TailPointerP):
        self.QueueArray = []
        self.HeadPointer = HeadPointerP
        self.TailPointer = TailPointerP
        for x in range(0, 100):
            self.QueueArray.append(-1)

TheQueue = Queue(-1,0)

def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer() == -1:
        AQueue[AQueue.TailPointer()] = TheData
        AQueue.HeadPointer() = 0
        AQueue. TailPointer() += 1
        return 1
    else:
        if AQueue.TailPointer() > 99:
            return -1
        else: 
            AQueue.QueueArray[AQueue.TailPointer()] = TheData
            AQueue.TailPointer() = AQueue.TailPointer()+1
            return 1
        
def ReturnAllData():
    String = ""
    for x in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        Data = TheQueue[x].QueueArray[x] 
        String = (String+ " "+  str(Data))
    return String