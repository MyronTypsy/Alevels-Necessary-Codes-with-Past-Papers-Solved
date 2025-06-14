#creating a new file and then storing the given input
with open("EventGuest.txt", "r") as file :
    for i in range(0, 4):
        
        print(file.readline().strip())
file.close()

#find out how you can read only 2 lines
