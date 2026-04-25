
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can safely remove an instance from list1 that has the same number as in list2
list1.remove(list2[0])  # This will now work as intended

# Check list1 contents after removal
for obj in list1:
    print(obj.number)
