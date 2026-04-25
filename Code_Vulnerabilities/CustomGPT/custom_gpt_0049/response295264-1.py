
def __str__(self):
    self.cardList = []
    for compID, number in self.cards.items():
        final = compID + "-" + str(number)
        self.cardList.append(final)  # Fixed this line to use 'final'

    self.cardList.sort()  # Sorting the list
    return self.tile + ": Card scores: [ " + ", ".join(self.cardList) + " ]"
