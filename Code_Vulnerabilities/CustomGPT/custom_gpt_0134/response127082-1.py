
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        # Check if the other object is an instance of move and compare the numbers
        return isinstance(other, move) and self.number == other.number

# Create two lists of move objects
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the first instance of list2 from list1
list1.remove(list2[0])

# Output the remaining elements in list1
for m in list1:
    print(m.number)  # Should print 1, 2, and 4
