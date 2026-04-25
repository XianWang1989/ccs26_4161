
class User:
    def __init__(self, title):
        self.tile = title
        self.cards = {}

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = compID + "-" + str(number)
            self.cardList.append(final)  # Use 'final' instead of 'temp'
        self.cardList.sort()
        # Format the card list to not include single quotes
        return self.tile + ": Card scores: [ " + ", ".join(self.cardList) + " ]"

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)  # Output should be formatted as you want
print(user2)  # Output should also be formatted
