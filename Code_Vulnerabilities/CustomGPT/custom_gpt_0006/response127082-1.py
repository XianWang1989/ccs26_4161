
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now we can remove an instance based on its attribute
list1.remove(list2[0])  # This will work now

# Verifying the result
for move in list1:
    print(move.number)  # Output should be: 1, 2, 4
