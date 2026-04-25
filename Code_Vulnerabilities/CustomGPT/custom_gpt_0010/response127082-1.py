
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

    def __hash__(self):
        return hash(self.number)

# Create instances
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now you can remove an instance based on its attribute
list1.remove(list2[0])  # This will work now

# To confirm the removal
for m in list1:
    print(m.number)  # This will print: 1, 2, 4
