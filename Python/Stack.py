'''
FILO
first in last out
#stack pointer represents the first empty space in stack

stack pointer 

""  4 
""  3
""  2
""  1 
""  0  <-- SP

""      4 
""      3
""      2
""      1  <-- SP
"Ruth"  0  

""      4 
""      3
""      2  <-- SP
"Yash"  1  
"Ruth"  0  
'''
Names = [""]* 5
SP = 0

def push(data):
    global SP
    global Names
    lenStack = 5
    if SP > lenStack:
        print("Stack is full")
    else:
        Names[SP] = data
        SP += 1

def pop():
    global SP
    global Names
    if SP == 0:
        print("Stack is Empty")
    else:
        Popped = Names[SP -1] = ""
        print(Popped)
        Names[SP -1] =""
        SP -=1
        
        
flag = True
while flag:
    inp = input("Enter Command a = push, b = pop, c = print")
    if inp == "a":
        val = input("Enter val to push")
        push(val)
    elif inp == "b":
        pop()
    elif inp == "c":
        print(Names)
        
'''

PUSH:
To perform the push operation, we first check if there is space available in the stack.
This is done by comparing tos (top of stack) with the maximum index of the array.
If the stack is full, we print a message saying "Stack is full".
If there is space, we increment tos and insert the new element at the updated tos position in the list.

POP:
If tos is 0, we say the stack is empty.
If it's not, we first store the item present at the current tos index.
Then, we reset or remove the item at that index (e.g., by setting it to None).
Finally, we decrement tos to reflect the removal of the top element.
'''