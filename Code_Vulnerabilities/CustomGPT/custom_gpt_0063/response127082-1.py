
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"move({self.number})"

# Example usage
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Now we can remove the instance based on its attribute
list1.remove(list2[0])

# Checking the result
print(list1)  # Output: [move(1), move(2), move(4)]
