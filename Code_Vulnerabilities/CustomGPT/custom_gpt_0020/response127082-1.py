
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

# Create two lists
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Attempt to remove an instance from list1 that has the same attribute value
list1.remove(list2[0])  # This will now work, as we've defined equality based on 'number'

# Output the updated list1 to confirm removal
for move_instance in list1:
    print(move_instance.number)
