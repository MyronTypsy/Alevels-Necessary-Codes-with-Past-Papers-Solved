'''#SLICING
name = "ruth fatima"
print(name[0:4])
print(name[5:14])
print(name[1])

#LENGTH
name1 = "Ruth"
temp = len(name1)
print(temp)'''

fname= input("Enter name ")

lent = len(fname)

for x in range(0,lent):
    
    if fname[x]== " ":
        temp= fname[0:x]
        print("first name " ,temp)
       
    
        temp2 = fname[x+1:lent]
        
        print("last name", temp2)

