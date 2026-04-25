
class Move(object):
    def __init__(self, number):
        self.number = number

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Filter out the move from list1 whose number matches that of list2[0]
list1 = [move for move in list1 if move.number != list2[0].number]
print([move.number for move in list1])  # Output: [1, 2, 4]
