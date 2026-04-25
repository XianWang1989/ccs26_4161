
class User:
    def __init__(self, title):
        self.title = title  # Fixed a typo here from 'tile' to 'title'
        self.cards = {}     # Initialize self.cards instead of self.rank

    def addCard(self, compID, number):
        if compID in self.cards and number > self.cards[compID]:
            self.cards[compID] = number
        elif compID not in self.cards:
            self.cards[compID] = number   

    def __str__(self):
        self.cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"  # Formatting for the card representation
            self.cardList.append(final)
        self.cardList.sort()

        # Join the cardList items as a single string with the desired formatting
        card_list_str = ', '.join(self.cardList)  # Joining without quotes
        return f"{self.title}: Card scores: [ {card_list_str} ]"  # Final output format

# Example usage
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)
print(user2)
