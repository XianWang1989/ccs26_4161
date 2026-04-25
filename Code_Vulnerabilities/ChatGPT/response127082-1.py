
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"move({self.number})"

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the instance from list1 that matches the number in list2[0]
list1 = [m for m in list1 if m != list2[0]]  # Using a list comprehension to filter list1

print(list1)  # Output will be: [move(1), move(2), move(4)]
