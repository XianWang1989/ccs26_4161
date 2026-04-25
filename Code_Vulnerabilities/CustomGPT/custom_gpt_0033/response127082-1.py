
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Use a loop to remove instances that match
for item in list2:
    try:
        list1.remove(item)
    except ValueError:
        pass  # Ignore if the item is not found

# Display the updated list1
for move in list1:
    print(move.number)
