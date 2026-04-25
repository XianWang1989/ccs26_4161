
class Move:
    def __init__(self, number):
        self.number = number

# Create lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Function to remove instances based on attribute
def remove_instances(source_list, to_remove_list):
    source_list[:] = [item for item in source_list if item.number not in {instance.number for instance in to_remove_list}]

# Remove instances from list1 based on list2
remove_instances(list1, list2)

# Display remaining items in list1
for move in list1:
    print(move.number)
