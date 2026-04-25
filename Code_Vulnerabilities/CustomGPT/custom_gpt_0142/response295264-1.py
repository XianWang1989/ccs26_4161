
class User:
    def __init__(self, title):
        self.title = title
        self.cards = {}  # Correct the attribute name

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"  # Use f-string for cleaner syntax
            self.cardList.append(final)

        self.cardList.sort()
        # Join the items in the cardList with ', ' and format the output
        return self.title + ": Card scores: [" + ", ".join(self.cardList) + "]"

# Example usage:
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)  # Output: Cpt.Fred: Card scores: [diamond-22, hearts-4, spades-3]
print(user2)  # Output: Lt.Connor: Card scores: [diamond-43]
