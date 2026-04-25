
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

# Create two lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the first instance of list2 from list1
item_to_remove = list2[0]  # Move(3)
if item_to_remove in list1:
    list1.remove(item_to_remove)

# Show the remaining items in list1
for move in list1:
    print(move.number)
