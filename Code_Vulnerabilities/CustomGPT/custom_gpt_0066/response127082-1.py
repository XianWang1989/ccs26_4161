
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can remove the instance of Move from list1
list1.remove(list2[0])

# Print the remaining elements in list1 to verify
for move in list1:
    print(move.number)
