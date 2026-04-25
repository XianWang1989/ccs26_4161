
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

# You can now remove the instance from list1 that matches list2[0]
list1.remove(list2[0])

print([move.number for move in list1])  # Output: [1, 2, 4]
