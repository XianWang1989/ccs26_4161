
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the instance from list1 based on matching attribute
for item in list2:
    # Check if there is a move with the same number and remove it
    list1 = [m for m in list1 if m.number != item.number]

print([m.number for m in list1])  # Output: [1, 2, 4]
