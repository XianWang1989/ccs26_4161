
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        # Check if 'other' is an instance of Move and compare the 'number' attribute
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"Move({self.number})"

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can remove the instance from list1
list1.remove(list2[0])  # This will work now

print(list1)  # Output: [Move(1), Move(2), Move(4)]
