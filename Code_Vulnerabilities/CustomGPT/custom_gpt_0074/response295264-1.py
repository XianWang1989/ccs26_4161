
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
            self.cardList.append(final)  # Change 'temp' to 'final'

        # Sort the list of cards
        self.cardList.sort()

        # Join the list into a single string without quotes
        return self.title + ": Card scores: [ " + ", ".join(self.cardList) + " ]"
