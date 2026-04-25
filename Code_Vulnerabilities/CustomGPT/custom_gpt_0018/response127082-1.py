
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now you can remove the instance from list1
list1.remove(list2[0])  # This will work without errors now
print([m.number for m in list1])  # Outputs: [1, 2, 4]
