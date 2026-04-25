
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
        self.cardList = []
        for compID, number in self.cards.items():
            final = compID + "-" + str(number)
            self.cardList.append(final)  # Fixed variable name from temp to final
        self.cardList.sort()
        formatted_cards = ", ".join(self.cardList)  # Join without quotes
        return f"{self.title}: Card scores: [ {formatted_cards} ]"
