
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __hash__(self):
        return hash(self.number)

# Create lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove an instance from list1 that matches list2[0]
list1.remove(list2[0])  # This will work now

# Display the remaining elements in list1
for move in list1:
    print(move.number)
