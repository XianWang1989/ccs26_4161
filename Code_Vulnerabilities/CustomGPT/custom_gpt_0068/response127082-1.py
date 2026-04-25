
class Move(object):
    def __init__(self, number):
        self.number = number

# Create two lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances in list1 that have a number present in list2
list1 = [item for item in list1 if item.number not in [m.number for m in list2]]

# Check the results
for move in list1:
    print(move.number)
