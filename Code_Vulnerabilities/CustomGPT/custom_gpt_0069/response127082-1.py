
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

# Example usage
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the move instance from list1
list1.remove(list2[0])  # This will now work without error

# Output the remaining instances in list1
for m in list1:
    print(m.number)  # Should print 1, 2, 4
