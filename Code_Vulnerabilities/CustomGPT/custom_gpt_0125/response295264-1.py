
class User:
    def __init__(self, title):
        self.tile = title
        self.cards = {}

    def addCard(self, compID, number):
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
        return f"{self.tile}: Card scores: [ {', '.join(self.cardList)} ]"
