
class Move(object):
    def __init__(self, number):
        self.number = number

    # This method will help in comparison based on the number
    def __eq__(self, other):
        return isinstance(other, Move) and self.number == other.number

# Create instances of Move
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Function to remove instances from the first list based on the attribute
def remove_instance_from_list(source_list, instance_to_remove):
    for item in source_list:
        if item == instance_to_remove:
            source_list.remove(item)
            break  # Exit after removing the first matching item

# Removing the instance from list1
remove_instance_from_list(list1, list2[0])

# Print the remaining items in list1
for move in list1:
    print(move.number)
