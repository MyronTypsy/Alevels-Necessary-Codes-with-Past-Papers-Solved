global Animal
global Colour
Animal  = [" "]*20
Colour =[" "]*20
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global Animal 
    global Colour
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global Animal
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        
        AnimalTopPointer -=1
        ReturnData = Animal[AnimalTopPointer]
        return ReturnData

def ReadAnimalData():
    try:
        global AnimalTopPointer
        global ColourTopPointer
        Animalfile = open("AnimalData.txt", "r")
        for Line in Animalfile:
            PushAnimal(Line.strip())      
        Animalfile.close()  
    except IOError:
        print("file not found")
        
def PushColour(DataToPush):
    global Animal
    global Colour
    
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

def PopColour():
    global Animal
    global Colour
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        
        ColourTopPointer -=1
        ReturnDataValue = Colour[ColourTopPointer]
        return ReturnDataValue

def ReadColourData():
    global Animal
    global Colour
    global AnimalTopPointer
    global ColourTopPointer
    try:
        file = open("ColourData.txt", "r")
        for Line in file:
            PushColour(Line.strip())
        file.close()        
    except IOError:
        print("file not found")
        
def OutputItem():
    global AnimalTopPointer
    global ColourTopPointer
    ColourReturned = PopColour()
    AnimalReturned = PopAnimal()
    if ColourReturned == "":
        print("No colour")
        PushAnimal(AnimalReturned)
    else:
        if AnimalReturned == "":
            print("No animal")
            PushColour(ColourReturned)
        else:  
            combine = ColourReturned + " " + AnimalReturned
            print(combine)
        
ReadAnimalData()
ReadColourData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()