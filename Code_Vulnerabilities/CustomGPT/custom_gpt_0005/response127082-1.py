
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now you can remove the instance based on the attribute
list1.remove(list2[0])

# Display the remaining elements in list1
for m in list1:
    print(m.number)  # Output: 1, 2, 4
