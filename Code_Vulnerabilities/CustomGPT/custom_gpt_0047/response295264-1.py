
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
            card_list.append(f"{compID}-{number}")
        card_list.sort()
        return f"{self.title}: Card scores: [ {', '.join(card_list)} ]"
