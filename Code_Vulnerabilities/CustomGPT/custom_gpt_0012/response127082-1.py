
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now you can remove by creating an instance of move with the same number
list1.remove(move(list2[0].number))

print([m.number for m in list1])  # Output: [1, 2, 4]
