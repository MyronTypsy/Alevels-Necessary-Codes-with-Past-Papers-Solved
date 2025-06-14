class Card():
    #PRIVATE Number: Integer
    #PRIVATE Colour : String
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP
        self.__Colour = ColourP
    def GetNumber(self):
         return self.__Number
     
    def GetColour(self):
        return self.__Colour

OneRed = Card(1, "Red")
TwoRed = Card(2, "Red")
ThreeRed = Card(3, "Red")
FourRed = Card(4, "Red")
FiveRed = Card(5, "Red")
OneBlue = Card(1, "Blue")
TwoBlue = Card(2, "Blue")
ThreeBlue = Card(3, "Blue")
FourBlue = Card(4, "Blue")
FiveBlue = Card(5, "Blue")
OneYellow = Card(1, "Yellow")
TwoYellow = Card(2, "Yellow")
ThreeYellow = Card(3, "Yellow")
FourYellow= Card(4, "Yellow")
FiveYellow = Card(5, "Yellow")

class Hand():
    #PRIVATE Cards : ARRAY[0:9] OF Cards
    #PRIVATE FirstCard : INTEGER
    #PRIVATE NumberCards : INTEGER
    def __init__(self,Card1 , Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)

        self.__FirstCard = 0
        self.__NumberCards = 5
       
    def GetCards(self, Index):
        return self.__Cards[Index]
    
Player1 = Hand(OneRed, TwoRed,ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow,OneBlue)
Score = 0

def CalculateValue(HandObject):
    global Score
    Index = 0
    while Index <5:
        HandCard = HandObject.GetCards(Index)
        colour = HandCard.GetColour()
        number = HandCard.GetNumber()
        if colour == "Red":
            Score = Score + 5
        elif colour == "Blue":
            Score = Score + 10
        else: 
            Score = Score + 15
        Index = Index +1
    return Score

Score1 = CalculateValue(Player1)
Score2 = CalculateValue(Player2)

if Score1> Score2:
    print("Player 1 wins")
else:
    print("Player2 wins")
