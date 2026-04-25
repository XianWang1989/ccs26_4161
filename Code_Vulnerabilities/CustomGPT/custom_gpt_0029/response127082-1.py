
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Find the instance with the same number in list1 as in list2
instance_to_remove = next((m for m in list1 if m == list2[0]), None)

if instance_to_remove:
    list1.remove(instance_to_remove)

print([m.number for m in list1])  # Output: [1, 2, 4]
