
class User:
    def __init__(self, title):
        self.title = title
        self.cards = {}  # Note: Changed from `rank` to `cards` based on context

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            # Create the card representation
            final = f"{compID}-{number}"
            self.cardList.append(final)

        # Sort the card list
        self.cardList.sort()

        # Format the output without quotes
        card_scores = ', '.join(self.cardList)
        return f"{self.title}: Card scores: [ {card_scores} ]"

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamonds", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamonds", 43)

print(user1)  # Cpt.Fred: Card scores: [ diamonds-22, hearts-4, spades-3 ]
print(user2)  # Lt.Connor: Card scores: [ diamonds-43 ]
