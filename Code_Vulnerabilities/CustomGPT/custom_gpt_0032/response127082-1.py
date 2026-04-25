
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1 that has the same number as the one in list2
try:
    list1.remove(list2[0])
except ValueError:
    print("Instance not found in list1")

# Display the remaining instances in list1
for move in list1:
    print(move.number)
