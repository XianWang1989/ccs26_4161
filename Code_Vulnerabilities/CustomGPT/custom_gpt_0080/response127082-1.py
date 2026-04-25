
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        # Compare based on the number attribute
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1 that matches the number in list2[0]
list1.remove(list2[0])

print([m.number for m in list1])  # Output: [1, 2, 4]
