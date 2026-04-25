
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Create a function to remove an instance with the same number
def remove_instance(lst, instance):
    for item in lst:
        if item == instance:
            lst.remove(item)
            break  # Remove only the first occurrence

remove_instance(list1, list2[0])

# Display the remaining elements in list1
for move in list1:
    print(move.number)
