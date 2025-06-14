global StackVowel
global stackConsonant
StackVowel=[]
stackConsonant=[]
global VowelTop
global  ConsonantTop
ConsonantTop=0
VowelTop=0
def PushData(letter):
    global VowelTop
    global ConsonantTop
    global StackVowel
    global stackConsonant
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o'or letter == 'u':
        if VowelTop== 100:
            print("the stack for vowels is full")
        else:
            StackVowel.append(letter)
            VowelTop=VowelTop+1
    else:
        if ConsonantTop == 100:
            print("the stack for consonants is full")
        else:
            stackConsonant.append(letter)
            ConsonantTop=ConsonantTop+1
def ReadData():
    global StackVowel
    global stackConsonant
    global VowelTop
    global ConsonantTop
    try:
        MyFile= open("StackData.txt",'r')
        for line in MyFile:
            PushData(line)
        MyFile.close()
    except IOError:
        print("file does not exist")
def PopVowel():
    global VowelTop
    global ConsonantTop
    global StackVowel
    global stackConsonant
    if VowelTop==0:
        return("No data")
    else:
        VowelTop = VowelTop - 1 # since it already points to next available space so we need to decreament it first
        RemovedVowel= StackVowel[VowelTop]
        del StackVowel[-1]
        return RemovedVowel
def PopConsonant():
    global VowelTop
    global ConsonantTop
    global StackVowel
    global stackConsonant
    if ConsonantTop==0:
        print("No Data")
    else:
        ConsonantTop = ConsonantTop - 1
        RemovedConsonant = stackConsonant[ConsonantTop]
        del stackConsonant[-1]
        return RemovedConsonant
ReadData()
Final = " "
myletter = ""
Empty= False
for x in range(5):
    Empty= False
    while Empty == False:
        UserLetter= input("please enter whether you wish to remove a vowel or a consonant")
        if UserLetter.lower() == "vowel":
            myletter= PopVowel()
            if myletter != "No Data":
                Final += myletter
                Empty=True
            else:
                print("no more vowels to remove ")
        elif UserLetter.lower() == "consonant" :
            myletter=PopConsonant()
            if myletter != "No Data":
                Final= Final + myletter
                Empty=True
            else:
                print("no more consonants to remove ")
print(Final)





