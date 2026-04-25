
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove an instance from list1 that matches the attributes of list2[0]
try:
    list1.remove(list2[0])
    print("Removed:", list2[0].number)
except ValueError:
    print("Value not found in list1.")

# Display the remaining elements in list1
for move in list1:
    print("Remaining in list1:", move.number)
