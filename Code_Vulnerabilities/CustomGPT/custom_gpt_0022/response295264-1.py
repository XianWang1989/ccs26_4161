
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
        card_list = []
        for compID, number in sorted(self.cards.items()):
            final = f"{compID}-{number}"  # Create formatted string
            card_list.append(final)

        # Join the list without quotes and format brackets
        return f"{self.tile}: Card scores: [ {' '.join(card_list)} ]"
