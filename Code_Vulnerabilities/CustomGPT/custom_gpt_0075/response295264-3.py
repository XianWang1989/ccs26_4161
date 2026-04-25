
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
        # Prepare output without quotes
        cardList = [f"{compID}-{number}" for compID, number in sorted(self.cards.items())]
        return f"{self.title}: Card scores: [ {', '.join(cardList)} ]"
