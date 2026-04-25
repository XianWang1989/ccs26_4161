
class Move:
    def __init__(self, number):
        self.number = number

# Create the lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances from list1 that have the same number as any in list2
list1 = [item for item in list1 if item.number not in [m.number for m in list2]]

# Display the resulting list1
for move in list1:
    print(move.number)
