
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __hash__(self):
        return hash(self.number)

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instance from list1 that matches the value in list2
list1 = [m for m in list1 if m != list2[0]]

# Output the remaining elements in list1
for move in list1:
    print(move.number)
