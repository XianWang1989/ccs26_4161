
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance from list1 that matches the first instance in list2
for item in list2:
    if item in list1:
        list1.remove(item)

print("Updated list1:", [m.number for m in list1])
