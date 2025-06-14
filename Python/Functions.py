#a void function and doesnt take input
def basicPrinter():
    print("i love myself")

basicPrinter()

def yourName(name):
    print(name)

yourName("Ruth")

#a non void function that takes an input

def plusOne(num):
    x = num + 1
    return x

age = plusOne(5)
print(age)

#smarter way
#always use a varaible to store the fuction when you use return and then print that
def plusOne(num):
    
    return num + 1

age = plusOne(5)
print(age)