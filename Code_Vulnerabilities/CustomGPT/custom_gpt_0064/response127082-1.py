
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

# Create lists
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove instance from list1 that is equal to list2[0]
list1.remove(list2[0])

# Output the remaining instances in list1
for m in list1:
    print(m.number)
