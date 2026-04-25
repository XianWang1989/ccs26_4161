
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
        # Create a list of formatted strings
        cardList = []
        for compID, number in self.cards.items():
            cardList.append(f"{compID}-{number}")

        # Sort the cardList
        cardList.sort()

        # Join the list without quotes and format the output
        formatted_list = ', '.join(cardList)
        return f"{self.title}: Card scores: [ {formatted_list} ]"
