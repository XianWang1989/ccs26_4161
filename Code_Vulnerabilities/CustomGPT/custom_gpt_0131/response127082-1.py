
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance with the same number
list1 = [item for item in list1 if item != list2[0]]

# Display the remaining items in list1
for item in list1:
    print(item.number)
