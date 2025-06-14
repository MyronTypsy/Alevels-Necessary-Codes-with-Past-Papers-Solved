Jobs=[]
global NumberOfJobs

def Initialise():
    global NumberOfJobs, Jobs
    NumberOfJobs = 0
    Jobs = [[-1, -1] for x in range(100)]

        

'''for x in range(100):
    print(Jobs[x][0], Jobs[x][1])'''
    
def AddJob(JobNumber, Priority):
    flag = False
    for x in range(100):
        if Jobs[x][0] == -1 and Jobs[x][1] == -1:
            Jobs[x][0] = JobNumber
            Jobs[x][1] = Priority
            flag = True
            print("Added")
            break  
    if flag == False :
        print("Not Added")

Initialise()

AddJob(12, 10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

def InsertionSort():
    global Jobs
    for i in range(1, 100):
        key = Jobs[i]
        x = i -1 
        while x >= 0 and key[1] < Jobs[x][1]:
            Jobs[x+1] = Jobs[x]
            x -= 1
        Jobs[x+1] = key
        
def PrintArray():
    for x in range(100):
        print(Jobs[x][0], "priority", Jobs[x][1])
        
InsertionSort()
PrintArray()