
def __str__(self):
    self.cardList = []
    for compID, number in self.cards.items():
        final = f"{compID}-{number}"  # Use f-string for formatting
        self.cardList.append(final)  # Corrected from 'temp' to 'final'
    self.cardList.sort()

    # Join the items without quotes and surround with brackets
    return f"{self.tile}: Card scores: [ {', '.join(self.cardList)} ]"
