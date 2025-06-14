class node():
    #Public data : INTEGER
    #Public nexNode : INTEGER
    def __init__(self, dataP, nextNodeP):
        self.data = dataP
        self.nextNode = nextNodeP
    
#DECLARE startPointer : Integer
#DECLARE emptyList : Integer
#DECLARE linkedlist : ARRAY[0:9] OF node
linkedlist = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),
 node(0,8),node(56,3),node(0,9),node(0,-1)] 

startPointer = 0
emptyList = 5

def outputNodes(linkedlist, startPointer):
    
    currentPointer = startPointer
    while currentPointer != -1:
        print(str(linkedlist[currentPointer].data))
        currentPointer = linkedlist[currentPointer].nextNode
        
outputNodes(linkedlist, 0)

def addNode(linkedlist,  currentPointer, emptyList):
    global startPointer
    data = int(input("please enter data"))
    if emptyList < 0 or emptyList> 9:
        return False
    else:
        freelist = emptyList
        emptyList = linkedlist[emptyList].nextNode
        
        newNode = node(data, -1)
        linkedlist[freelist] = newNode
        
        if startPointer == -1:  # Handle empty list case
            startPointer = freelist
        else:
            currentPointer = startPointer
            while linkedlist[currentPointer].nextNode != -1:
                currentPointer = linkedlist[currentPointer].nextNode
        linkedlist[currentPointer].nextNode = freelist 

        return True

outputNodes(linkedlist, 0)
addNode(linkedlist, 0, 5)
outputNodes(linkedlist, 0)
