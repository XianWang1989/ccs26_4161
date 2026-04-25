
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Finding an instance in list1 that is equal to list2[0] based on the number
instance_to_remove = None
for item in list1:
    if item == list2[0]:
        instance_to_remove = item
        break

if instance_to_remove:
    list1.remove(instance_to_remove)

print([move.number for move in list1])  # Output: [1, 2, 4]
