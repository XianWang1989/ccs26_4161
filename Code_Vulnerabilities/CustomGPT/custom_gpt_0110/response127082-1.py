
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

# Remove the item from list1 that matches the one in list2
if list2[0] in list1:
    list1.remove(list2[0])

# Print remaining items in list1
for m in list1:
    print(m.number)
