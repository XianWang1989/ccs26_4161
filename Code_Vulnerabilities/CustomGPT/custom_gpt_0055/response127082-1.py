
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return isinstance(other, Move) and self.number == other.number

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instance from list1 that matches the first instance of list2
list1.remove(list2[0])  # This will now work without error

print("Updated list1:")
for move in list1:
    print(move.number)
