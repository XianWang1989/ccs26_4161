
class User:
    def __init__(self, title):
        self.title = title  # Fixed typo from 'tile' to 'title'
        self.cards = {}  # Initialize 'cards' dictionary

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = compID + "-" + str(number)  # Create card representation
            self.cardList.append(final)  # Append the formatted string to the list
        self.cardList.sort()  # Sort the card list
        return self.title + ": Card scores: [ " + ", ".join(self.cardList) + " ]"  # Format output without quotes

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)  # Outputs: Cpt.Fred: Card scores: [ diamond-22, hearts-4, spades-3 ]
print(user2)  # Outputs: Lt.Connor: Card scores: [ diamond-43 ]
