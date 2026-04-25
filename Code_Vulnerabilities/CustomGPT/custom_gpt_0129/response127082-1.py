
class Move(object):
    def __init__(self, number):
        self.number = number

# Create the lists of move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances from list1 based on the 'number' attribute of the first element in list2
number_to_remove = list2[0].number

# Use a list comprehension to filter out the instance with the matching number
list1 = [move for move in list1 if move.number != number_to_remove]

# Display the remaining elements in list1
print([move.number for move in list1])  # Output: [1, 2, 4]
