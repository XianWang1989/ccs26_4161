
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Use a list comprehension to remove instances in list2 from list1
list1 = [item for item in list1 if item not in list2]

# Display the remaining items in list1
for m in list1:
    print(m.number)
