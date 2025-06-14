'''
class is a blueprint for creating objects
creating a class
'''

class Book:
    def __init__(self, inputtedName, inputtedAuthor, Genre, Publisher, x):
        self.name = inputtedName
        self.Author = inputtedAuthor
        self.Genre = Genre
        self.Publisher = Publisher 
        self.YearOfPub = x

book1 = Book("LOTR", "JRR Tolkein", "Fantasty", "KGM Publications", "1800")
book2 = Book("Shandar Mobile", "Arbaz", "Motivational", "Shera", "2024")

print(book1.name)

#Ecapsulation in Python
class YTchannel:
    #PRIVATE Subscriber: INTEGER
    def __init__(self, Name, VidCount, SubCount):
        self.Name = Name
        self.VidCount = VidCount
        self.__Subscribers = SubCount
    
    def setSubscribers(self, count):
        self.__Subscribers = count
    
    def getSubscribers(self):
        return self.__Subscribers

ch1 = YTchannel("Zainmatics", "808", 98999) 
print(ch1.Name)       

ch1.setSubscribers(100000)

print(ch1.getSubscribers())
