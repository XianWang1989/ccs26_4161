
class User:
    def __init__(self, title):
        self.title = title
        self.cards = {}  # Changed to 'cards' from 'rank' to align with the logic

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"  # Create the final string for the card
            self.cardList.append(final)
        self.cardList.sort()

        # Manually constructing the string for cardList
        card_list_str = ", ".join(self.cardList)  # Join without quotes
        return f"{self.title}: Card scores: [ {card_list_str} ]"

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)  # Output: Cpt.Fred: Card scores: [ diamond-22, hearts-4, spades-3 ]
print(user2)  # Output: Lt.Connor: Card scores: [ diamond-43 ]
