
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"Move({self.number})"

# Create lists of instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances found in list2 from list1
for item in list2:
    if item in list1:
        list1.remove(item)

print(list1)  # Output should be: [Move(1), Move(2), Move(4)]
