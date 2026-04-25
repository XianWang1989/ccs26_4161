
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

# Create instances of Move
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances from list1 that match instances in list2
for item in list2:
    if item in list1:
        list1.remove(item)

# Output remaining elements in list1
for move in list1:
    print(move.number)
