
class Move:
    def __init__(self, number):
        self.number = number

# Create two lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Function to remove instances based on attribute
def remove_instances(source_list, to_remove_list):
    to_remove_numbers = {item.number for item in to_remove_list}
    return [item for item in source_list if item.number not in to_remove_numbers]

# Update list1 by removing instances present in list2
list1 = remove_instances(list1, list2)

# Verify the result
for move in list1:
    print(move.number)  # Output: 1, 2, 4
