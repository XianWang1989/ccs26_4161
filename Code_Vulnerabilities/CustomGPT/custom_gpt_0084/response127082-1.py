
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        # Check if the other object is an instance of Move and has the same number
        return isinstance(other, Move) and self.number == other.number

# Create the lists
list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove the first instance in list2 from list1
list1.remove(list2[0])  # This will now work!

# Print the remaining items in list1 to verify
for move in list1:
    print(move.number)
