
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"Move({self.number})"

# Create instance lists
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1 using the content of list2
list1.remove(list2[0])  # This will now work correctly

print(list1)  # Output should reflect that Move(3) has been removed
