
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        # Check if 'other' is an instance of 'move' and compare their 'number' attributes
        if isinstance(other, move):
            return self.number == other.number
        return False

# Create two lists of move instances
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the instance from list1 that has the same 'number' as the instance in list2
list1.remove(list2[0])

# Confirm removal by printing the contents of list1
for move_instance in list1:
    print(move_instance.number)  # Output will be 1, 2, and 4, since 3 was removed
