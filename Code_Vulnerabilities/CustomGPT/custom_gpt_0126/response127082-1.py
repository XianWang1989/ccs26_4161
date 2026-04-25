
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return isinstance(other, Move) and self.number == other.number

# Create lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the first instance from list1 that matches the first instance in list2
list1.remove(list2[0])

# Display the remaining items in list1
for item in list1:
    print(item.number)
