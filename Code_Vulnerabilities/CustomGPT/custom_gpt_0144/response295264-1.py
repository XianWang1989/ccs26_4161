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
        cardList = []
        for compID, number in self.cards.items():
            final = f"{compID}-{number}"
            cardList.append(final)
        cardList.sort()
        # Join the card list into a custom string format
        cards_str = "[ " + ", ".join(cardList) + " ]"
        return f"{self.tile}: Card scores: {cards_str}"
