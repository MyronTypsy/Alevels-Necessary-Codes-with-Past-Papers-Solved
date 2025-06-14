class Card:
    #PRIVATE Number : INTEGER
    #PRIVATE Colour : STRING
    def __init__(self,NumberP, ColourP):
        self.__Number = NumberP
        self.__Colour =ColourP
    
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

class Hand():
    #PRIVATE Cards : ARRAY[0:9] OF CARD 
    #PRIVATE FirstHand : INTEGER
    #PRIVATE NumberCards : INTEGER
    
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2) 
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5) 
        self.__FirstHand = 0
        self.__NumberCards = 5
    
    def ReturnCard(self, Index):
        return self.__Cards[Index]
    
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed,
OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow,
FiveYellow, OneBlue)

def CalculateValue(Player):
    score = 0
    for y in range(5):
        CardGot = Player.ReturnCard(y)
        score = score + CardGot.GetNumber()
        colour = CardGot.GetColour()
        if colour == "red":
            score = score + 5
        elif colour == "blue":
            score = score + 10
        else:
            score = score + 15
        return score
    
Player1score = CalculateValue(Player1)
Player2score =CalculateValue(Player2)
if Player1score > Player2score:
 print("Player 1 wins")
elif Player1score < Player2score:
 print("Player 2 wins")
else:
 print("It's a draw")

        