
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

# Create lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1 that matches list2[0]
list1.remove(list2[0])

# Print the resulting list1 to verify the removal
for move in list1:
    print(move.number)  # Output should be: 1, 2, 4
