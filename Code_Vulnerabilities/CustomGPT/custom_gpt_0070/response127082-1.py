
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __hash__(self):
        return hash(self.number)

# Example usage
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Removing the instance from list1
list1.remove(list2[0])  # This works now

print([m.number for m in list1])  # Output: [1, 2, 4]
