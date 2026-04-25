
class User:
    def __init__(self, title):
        self.title = title  # Fixed property name from 'tile' to 'title'
        self.cards = {}     # Fixed property name from 'rank' to 'cards'

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"  # Using f-string for cleaner syntax
            self.cardList.append(final)    # Use final instead of temp which was undefined

        self.cardList.sort()  # Sort the list

        # Join the cardList elements without quotes
        return f"{self.title}: Card scores: [ {', '.join(self.cardList)} ]"

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)  # Output: Cpt.Fred: Card scores: [ diamond-22, hearts-4, spades-3 ]
print(user2)  # Output: Lt.Connor: Card scores: [ diamond-43 ]
