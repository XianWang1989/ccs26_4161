
class User:
    def __init__(self, title):
        self.title = title  # Fixed typo from 'tile' to 'title'
        self.cards = {}     # Initialized 'cards' attribute

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        card_list = []  # Create a new list for card representation
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"  # Format compID and number
            card_list.append(final)
        card_list.sort()  # Sort the list
        return f"{self.title}: Card scores: [ {', '.join(card_list)} ]"  # Format the output

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)
print(user2)
