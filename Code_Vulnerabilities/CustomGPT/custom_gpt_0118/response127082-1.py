
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1 that matches list2[0]
try:
    list1.remove(list2[0])
except ValueError as e:
    print(e)

# To confirm the removal
print([move.number for move in list1])  # Output should be [1, 2, 4]
