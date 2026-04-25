
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

# Create lists of move instances
list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove the first instance of list2 from list1
to_remove = list2[0]
# Finding the index of the instance to remove
for item in list1:
    if item == to_remove:
        list1.remove(item)
        break  # Remove this to allow removal of all identical items

# Display remaining elements in list1
remaining_numbers = [obj.number for obj in list1]
print("Remaining elements in list1:", remaining_numbers)
