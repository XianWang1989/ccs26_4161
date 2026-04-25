
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now you can safely remove the item
list1.remove(list2[0])

# Print out to see the result
print([m.number for m in list1])  # Output should be: [1, 2, 4]
