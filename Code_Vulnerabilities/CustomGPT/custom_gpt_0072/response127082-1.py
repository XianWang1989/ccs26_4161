
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        return self.number == other.number

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can remove an instance from list1 based on its value
list1.remove(list2[0])

# Print the remaining instances in list1
for move in list1:
    print(move.number)
