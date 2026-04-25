
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the element from list1 that has the same number as the first element in list2
list1.remove(list2[0])

print([move.number for move in list1])  # Output: [1, 2, 4]
