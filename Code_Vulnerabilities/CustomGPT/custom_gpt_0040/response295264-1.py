
class User:
    def __init__(self, title):
        self.title = title  # Corrected the variable name to title
        self.cards = {}  # Changed from self.rank to self.cards

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"  # Use f-string for better formatting
            cardList.append(final)
        cardList.sort()
        return f"{self.title}: Card scores: [ {', '.join(cardList)} ]"  # Join without quotes


# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)
print(user2)
