
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

# Sample lists
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove item from list1 that has the same number as the first item in list2
list1 = [item for item in list1 if item != list2[0]]

# Display the filtered list1
print([item.number for item in list1])  # Output: [1, 2, 4]
