
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return isinstance(other, Move) and self.number == other.number

    def __hash__(self):
        return hash(self.number)

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1
list1.remove(list2[0])

print([move.number for move in list1])  # Output will be [1, 2, 4]
