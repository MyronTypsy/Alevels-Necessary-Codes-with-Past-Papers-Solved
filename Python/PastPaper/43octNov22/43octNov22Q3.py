FreeNode= 6
RootPointer = 0
ArrayNodes = [[1,20,5],[2,15,-1], [-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1],[1,-1,-1]]
'''class ArrayNode():
    def __init__(self, LeftPointerP, DataP, RightPointerP):
        self.LeftPointer = LeftPointerP
        self.Data = DataP
        self.RightPointer = RightPointerP
    
Node1 = ArrayNode(1,20,5)
Node2 = ArrayNode(2,15,-1)
Node3 = ArrayNode(-1,3,3)
Node4 = ArrayNode(-1,9,4)
Node5 = ArrayNode(-1,10,-1)
Node6 = ArrayNode(-1,58,-1)
Node7 = ArrayNode(-1,-1,-1)
'''
def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1
    
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1]< ValueToFind:
        return SearchValue(ArrayNodes[Root][2],ValueToFind)
    
def PostOrder(Root):
    if Root == -1:
        return
    if ArrayNodes[Root][0] != -1:
        LeftRoot = ArrayNodes[Root][0]
        PostOrder(LeftRoot)

        PostOrder(LeftRoot)
    if ArrayNodes[Root][2] != -1:
        RightRoot = ArrayNodes[Root][2]
        PostOrder(RightRoot)

    print(ArrayNodes[Root][1])

Found = SearchValue(0,15)
if Found == -1:
    print("Number not found")
else:
    print("The number 15 is found at ", Found )
PostOrder(ArrayNodes[RootPointer])