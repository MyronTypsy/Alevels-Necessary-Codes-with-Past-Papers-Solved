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
    #gotta make startppointer global
    global startPointer
    data = int(input("please enter data : "))
    
    
    '''
    There are 2 lists one is empty and one is linked list
    the gist of adding in an ordered linked list is that we take the emptylist and we add it to the end of the linked list
    for doing that we need to point our tell the computer that our empty list index is now not the same soo we increment tahat by using the .nextnode
    
    Basically to add a node we have to a couple of steps
    Step 1: 
    check if we have space to add a node or not
    Step 2: 
    now we store the value of emptylist starting index in the freelist pointer which is freeindex
    Step 3:
    increment empty list
    Step 4:
    create a new node
    Step 5:
    use the free index to store data
    Step 6:
    now we just find the last node because we want it to link with the newly added node created by the user
    '''
    
    #check if there is space or not
    if emptyList < 0 or emptyList> 9:
        return False
    else:
        #now we store the value of emptylist starting index in the freelist pointer which is freeindex
        freeIndex = emptyList
        #increment empty list because the first node is now gonna be used to store data that the user provides
        emptyList = linkedlist[emptyList].nextNode
        
        #create a new node
        newNode = node(data, -1)
        #use the free index to store data 
        linkedlist[freeIndex] = newNode
        
        #now we just find the last node because we want it to link with the newly added node created by the user
        if startPointer == -1:  # Handle empty list case
            startPointer = freeIndex
        else:
            currentPointer = startPointer
            while linkedlist[currentPointer].nextNode != -1:
                currentPointer = linkedlist[currentPointer].nextNode
        linkedlist[currentPointer].nextNode = freeIndex 

        return True
print("previous list")
outputNodes(linkedlist, 0)

addNode(linkedlist, 0, 5)
print("new list")

outputNodes(linkedlist, 0)

