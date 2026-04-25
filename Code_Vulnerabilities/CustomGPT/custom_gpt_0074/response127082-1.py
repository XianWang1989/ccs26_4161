
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# We filter out instances from list1 that match the number in list2[0]
list1 = [item for item in list1 if item != list2[0]]

# Now list1 will not have the instance with number 3
print([m.number for m in list1])  # Output: [1, 2, 4]
