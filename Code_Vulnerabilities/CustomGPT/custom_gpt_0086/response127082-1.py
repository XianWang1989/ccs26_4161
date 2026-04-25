
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

# Create two lists of move instances
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the first instance from list1 that matches the first instance in list2
list1.remove(list2[0])

# Output the remaining elements in list1
for m in list1:
    print(m.number)
