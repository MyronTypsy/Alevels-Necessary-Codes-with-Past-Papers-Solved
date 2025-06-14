class Card():
    #PRIVATE Number : Integer
    #PRIVATE Colour : STRING
    def __init__(self,NumberP, ColourP):
        self.__Number = NumberP
        self.__ColourP = ColourP
    
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__ColourP
    
onered = Card(1,"red")
twored = Card(2,"red")
threered = Card(3,"red")
fourred = Card(4,"red")
fivered = Card(5,"red")
oneblue = Card(1,"blue")
twoblue = Card(2,"blue")
threeblue = Card(3,"blue")
fourblue = Card(4,"blue")
fiveblue = Card(5,"blue")
oneyellow = Card(1,"yellow")
twoyellow = Card(2,"yellow")
threeyellow = Card(3,"yellow")
fouryellow = Card(4,"yellow")
fiveyellow = Card(5,"yellow")


class Hand():
    def __init__(self,card0,card1, card2, card3, card4):
        self.__Cards = []
        self.__Cards.append(card0)
        self.__Cards.append(card1)
        self.__Cards.append(card2)
        self.__Cards.append(card3)
        self.__Cards.append(card4)
        self.__FirstHand = 0
        self.__NumberCards = 5
    
    def GetCard(self, Index):
        return self.__Cards[Index]
    
Player1 = Hand(onered, twored, threered, fourred, oneyellow)
Player2 = Hand(twoyellow, threeyellow, fouryellow, fiveyellow, oneblue)

def CalculateValue(PlayerHand):
    Value = 0
    for x in range(5):
        cardinhand = PlayerHand.GetCard(x)
        if cardinhand == onered or cardinhand == twored or cardinhand == threered or cardinhand == fourred or cardinhand == fivered  :
            Value += 5
        elif cardinhand == oneblue or cardinhand == twoblue or cardinhand == threeblue or cardinhand == fourblue or cardinhand == fiveblue  :
            Value += 10
        elif cardinhand == oneyellow or cardinhand == twoyellow or cardinhand == threeyellow or cardinhand == fouryellow or cardinhand == fiveyellow :
            Value +=15
    return Value

score1 = CalculateValue(Player1)
score2 = CalculateValue(Player2)
if score1> score2:
    print("Player 1 won")
elif score1 == score2:
    print("game was a draw")
else:
    print("Player 2 won")
    