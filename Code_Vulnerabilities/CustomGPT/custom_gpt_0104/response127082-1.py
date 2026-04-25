
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the instance from list1 that has the same number as list2[0]
list1 = [m for m in list1 if m != list2[0]]

# Display the result
for m in list1:
    print(m.number)
