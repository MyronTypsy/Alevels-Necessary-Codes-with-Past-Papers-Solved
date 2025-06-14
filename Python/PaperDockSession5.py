global queue
global HeadPointer
global TailPointer

HeadPointer = -1
TailPointer = 0
queue = []*100

def Enqueue(IntVal):
    global queue
    global HeadPointer
    global TailPointer
    if TailPointer >0 and TailPointer < 100:
        queue[TailPointer] = IntVal
        TailPointer += 1
        
        if HeadPointer == -1:
            HeadPointer = 0
      
        return True
    else:
     
        return False
    
def Dequeue():
    global queue
    global HeadPointer
    global TailPointer
    
    if HeadPointer== -1:
        print("Queue is empty")
        return False
    else:
        item = queue[HeadPointer]
        
        HeadPointer+=1
    if HeadPointer == TailPointer:
        TailPointer = 0
        HeadPointer = -1
        
finalflag = True
for j in range(1, 21):
    temp = Enqueue(j)
    if temp == False:
        finalflag = False
       
   
if finalflag == True:
    print("Sucessfull")
else:
    print("UnSucessfull")

print(queue)