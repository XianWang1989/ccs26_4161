
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

    def __repr__(self):  # Optional: For better representation
        return f"move({self.number})"

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now you can remove the instance from list1
list1.remove(list2[0])  # This will work now

print(list1)  # Output: [move(1), move(2), move(4)]
