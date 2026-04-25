
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __hash__(self):
        return hash(self.number)

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can remove the instance based on its value
list1.remove(list2[0])

# Output the modified list1
for move in list1:
    print(move.number)
