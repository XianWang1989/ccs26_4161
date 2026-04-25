
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Using list comprehension to filter out elements
list1 = [m for m in list1 if m not in list2]  # This will call __eq__

# Display resulting list1
for m in list1:
    print(m.number)  # Output will be: 1, 2, 4
