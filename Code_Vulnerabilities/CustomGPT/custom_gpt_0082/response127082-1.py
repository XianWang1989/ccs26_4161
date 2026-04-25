
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances from list1 based on their 'number' attribute
for item in list2:
    list1 = [x for x in list1 if x.number != item.number]

# Output the remaining elements in list1
for move in list1:
    print(move.number)
