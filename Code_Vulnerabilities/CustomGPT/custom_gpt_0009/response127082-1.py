
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Removing instances based on matching attribute
for move in list2:
    if move in list1:
        list1.remove(move)

# Checking the contents of list1
print([move.number for move in list1])  # Output: [1, 2, 4]
