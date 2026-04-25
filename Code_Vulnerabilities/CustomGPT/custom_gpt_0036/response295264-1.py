
class User:
    def __init__(self, title):
        self.title = title  # Fixed typo from 'tile' to 'title'
        self.cards = {}     # Initialize the cards dictionary

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"  # Use f-string for better formatting
            self.cardList.append(final)
        self.cardList.sort()  # Sort the list of card strings
        formatted_cards = ", ".join(self.cardList)  # Join the list without quotes
        return f"{self.title}: Card scores: [ {formatted_cards} ]"  # Return formatted string

# Example Usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)
print(user2)
