
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"Move({self.number})"

# Create lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove by value using the __eq__ method
item_to_remove = list2[0]  # Move(3)
if item_to_remove in list1:
    list1.remove(item_to_remove)

print(list1)  # Output will be [Move(1), Move(2), Move(4)]
