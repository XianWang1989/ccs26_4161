
class Move:
    def __init__(self, number):
        self.number = number

# Create lists of Move instances
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the instance based on the attribute
number_to_remove = list2[0].number
list1 = [move for move in list1 if move.number != number_to_remove]

# Output the remaining elements
for move in list1:
    print(move.number)  # Output: 1, 2, 4
