
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

# Now you can remove an item from list1 that has the same attribute
list1.remove(list2[0])  # Removes the instance move(3)

# Show the results
for move_instance in list1:
    print(move_instance.number)  # This should print numbers 1, 2, and 4
