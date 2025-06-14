global FirstNode
global FirstEmpty
global LinkedList
LinkedList = []
FirstNode = -1
FirstEmpty= 0
for x in range(19):
    LinkedList.append([-1,x+1])
LinkedList[19][0] =-1
LinkedList[19][1] =-1  

def InsertData():
    global FirstNode
    global FirstEmpty
    global LinkedList
    
    for x in range(5):
        while FirstEmpty != -1:
            NextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("Enter Data"))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = NextEmpty

def OutputLinkedList():
    global FirstNode
    global FirstEmpty
    global LinkedList
    currentPointer = FirstNode
    for x in range(20):
        print(LinkedList[x])