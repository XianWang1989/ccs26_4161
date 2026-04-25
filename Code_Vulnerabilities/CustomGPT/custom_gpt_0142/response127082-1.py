
class Move(object):
    def __init__(self, number):
        self.number = number

    # Override the __eq__ method to compare based on the number attribute
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    # Optional: Override the __repr__ method for better display of objects
    def __repr__(self):
        return f"Move({self.number})"

# Example usage:
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can safely remove an instance from list1
list1.remove(list2[0])  # This will work because __eq__ is defined

print("Updated list1:", list1)  # Should show [Move(1), Move(2), Move(4)]
