
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

# Create instances of Move
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance with the same attribute value
list1.remove(list2[0])

# Display the remaining elements in list1
for move in list1:
    print(move.number)  # Should output 1, 2, and 4
