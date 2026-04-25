
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __hash__(self):
        return hash(self.number)

# Create instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove an instance from list1 based on attribute comparison
item_to_remove = list2[0]
if item_to_remove in list1:
    list1.remove(item_to_remove)

# Output the remaining items in list1
for move in list1:
    print(move.number)  # Should output: 1, 2, 4
