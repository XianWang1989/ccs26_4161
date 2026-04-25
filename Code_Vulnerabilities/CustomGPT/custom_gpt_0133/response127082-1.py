
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

# Creating lists of move instances
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the instance from list1 that has the same number as the first instance in list2
list1.remove(list2[0])  # This will now work

print([m.number for m in list1])  # Output should be: [1, 2, 4]
