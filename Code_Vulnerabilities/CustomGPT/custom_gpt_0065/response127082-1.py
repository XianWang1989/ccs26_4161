
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the first instance in list1 that matches the number in list2[0]
list1 = [item for item in list1 if item != list2[0]]

# Display the updated list1
for move in list1:
    print(move.number)
