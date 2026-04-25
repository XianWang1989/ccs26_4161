
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

# Create the lists
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1 that has the same attribute as list2[0]
list1 = [item for item in list1 if item != list2[0]]

# Displaying the remaining elements in list1
for move in list1:
    print(move.number)
