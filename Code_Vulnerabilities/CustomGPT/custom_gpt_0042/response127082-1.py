
class Move:
    def __init__(self, number):
        self.number = number

    # Override the equality method
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can remove an instance from list1
list1.remove(list2[0])  # This will work now

# Let's print the remaining items in list1 to confirm
for move in list1:
    print(move.number)
