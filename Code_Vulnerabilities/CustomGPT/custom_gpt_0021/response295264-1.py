
class User:
    def __init__(self, title):
        self.title = title
        self.cards = {}

    def add_card(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"
            self.cardList.append(final)
        self.cardList.sort()
        # Join without quotes and format with brackets
        return f"{self.title}: Card scores: [ {', '.join(self.cardList)} ]"

# Example usage
user1 = User("Cpt.Fred")
user1.add_card("diamond", 22)
user1.add_card("hearts", 4)
user1.add_card("spades", 3)

user2 = User("Lt.Connor")
user2.add_card("diamond", 43)

print(user1)
print(user2)
