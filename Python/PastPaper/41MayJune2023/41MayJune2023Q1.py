# Initialize an empty list to store data read from the file
dataArray = []

# Try to open the file and read its contents
try:
    file = open("Data.txt", "r")  # Open the file named "Data.txt" in read mode
    
    # Read each line from the file, strip newline characters, and add to the list
    for Line in file:
        dataArray.append(Line.strip())
    
    file.close()  # Close the file after reading
except IOError:
    # If the file cannot be found or opened, print an error message
    print("File could not be found")

# Define a function to print all values in the array in a single line
def PrintArray(dataArray):
    output = ""
    for x in range(0, len(dataArray)):
        output = output + str(dataArray[x]) + " "  # Concatenate each value with a space
    print(output)  # Print the final string

# Call the function to display the contents of the array
PrintArray(dataArray)

# Define a function to count how many times a given number appears in the array
def LinearSearch(dataArray, IntSearchVal):
    count = 0
    for x in range(len(dataArray)):
        if dataArray[x] == str(IntSearchVal):  # Compare as string because file data is string
            count = count + 1
    return count  # Return how many times the number was found

# Ask the user to enter a number between 0 and 100
val = int(input("Enter a number between 0 and 100: "))

# Keep asking until the input is valid
while val < 0 or val > 100:
    val = int(input("Wrong input. Please enter a number between 0 and 100: "))

# Call the LinearSearch function to count occurrences of the number
NumberTimes = LinearSearch(dataArray, val)

# Print the result
print("The number", val, "is found", NumberTimes, "times.")
