
class move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return isinstance(other, move) and self.number == other.number

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the instance from list1 that matches the number in list2
list1.remove(list2[0])  # This will work now

# Print remaining elements in list1 to verify
for item in list1:
    print(item.number)
