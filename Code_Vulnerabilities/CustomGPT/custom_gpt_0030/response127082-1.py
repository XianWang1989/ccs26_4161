
class Move(object):
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

# Remove the instance from list1 that matches the one in list2
list1.remove(list2[0])  # This works now because of the equality defined.

# Output the remaining elements in list1 to verify
for move in list1:
    print(move.number)
