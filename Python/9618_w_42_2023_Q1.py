StackVowel = []*100
StackConsonants = []*100


global VowelTop
global ConsonantTop
VowelTop = 0 #stores index of free space
ConsonantTop = 0 #stores index of free space

def PushData(letter):
    global VowelTop
    global ConsonantTop
    if (letter == "a") or (letter== "e") or (letter== "i") or (letter== "o") or (letter== "u"):
        if VowelTop <100:    
            StackVowel.append(letter)
            VowelTop += 1
        else:
            print("vowel stack is full")
    else :
        if ConsonantTop < 100:
            StackConsonants.append(letter)
            ConsonantTop+=1
        else:
            print("consonants stack is full")
        
def ReadData():
    global VowelTop
    global ConsonantTop
    try:
        file = open("StackData.txt","r")
        for x in range(0,100):
            data = file.readline().strip()
            PushData(data)
        file.close()
    except IOError:
        print("file not found")
        
def PopVowel():
    global VowelTop
    global ConsonantTop
    VowelTop -= 1
    if VowelTop != 0:
        popped = StackVowel[VowelTop] 
        return popped
    else:
        return "No Data"
    
def PopConsonant():
    global VowelTop
    global ConsonantTop
    ConsonantTop -= 1
    if ConsonantTop != 0 :
        popped = StackConsonants[ConsonantTop] 
        return popped
    else:
        return "No Data"
    
ReadData()
Letters = ""
VowelTop = 0
ConsonantTop = 0
for x in range(0, 5):
    Flag = False
    while Flag == False:
        choice = input("enter a vowel or a consonant").lower()
        if choice == "vowel":
            DataAccessed = PopVowel()
            if DataAccessed != "No data":
                Letters = Letters + DataAccessed
                Flag = True
            else:
                print("No vowels left")
        elif choice == "consonant":
            DataAccessed = PopConsonant()
        if DataAccessed != "No data":
            Letters = Letters + DataAccessed
            Flag = True
        else:
            print("No consonants left")
print(Letters)
