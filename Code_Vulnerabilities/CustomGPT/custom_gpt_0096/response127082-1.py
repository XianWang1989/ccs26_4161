
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

# Create instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1
list1.remove(list2[0])  # This will now work without an error

# Printing the modified list1 to confirm removal
for move in list1:
    print(move.number)
