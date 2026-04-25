
class Move:
    def __init__(self, number):
        self.number = number

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Method to remove an instance based on its attribute value
def remove_instance(list_to_modify, instance):
    for item in list_to_modify:
        if item.number == instance.number:  # Compare based on attribute
            list_to_modify.remove(item)
            break  # Stop after removing the first match

remove_instance(list1, list2[0])  # Remove the instance with number 3

# Printing the result
for move in list1:
    print(move.number)  # Output: 1, 2, 4
