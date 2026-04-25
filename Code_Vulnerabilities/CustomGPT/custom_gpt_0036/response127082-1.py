
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now using a loop to remove instances based on attribute
for item in list2:
    if item in list1:  # This will now call the __eq__ method
        list1.remove(item)

# Display resulting list1
for m in list1:
    print(m.number)  # Output will be: 1, 2, 4
