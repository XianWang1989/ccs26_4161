
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance with the same attribute from list1
list1 = [item for item in list1 if item not in list2]

# Check the modified list1
for move in list1:
    print(move.number)  # Output: 1, 2, 4
