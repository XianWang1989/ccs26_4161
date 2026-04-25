
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

# Sample lists
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove using the matching attribute
list1 = [item for item in list1 if item not in list2]

# Resulting list1
for move in list1:
    print(move.number)  # Should print 1, 2, 4
