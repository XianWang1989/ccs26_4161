
class User:
    def __init__(self, title):
        self.title = title
        self.cards = {}

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        card_list = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"
            card_list.append(final)
        card_list.sort()
        return f"{self.title}: Card scores: [{', '.join(card_list)}]"

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)
print(user2)
