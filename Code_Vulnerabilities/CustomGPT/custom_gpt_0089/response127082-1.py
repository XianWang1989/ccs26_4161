
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"Move({self.number})"

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Now you can safely remove the instance
list1.remove(list2[0])

print(list1)  # Output: [Move(1), Move(2), Move(4)]
