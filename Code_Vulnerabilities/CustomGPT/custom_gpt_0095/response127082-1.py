
class Move:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.number == other.number
        return False

    def __repr__(self):
        return f"Move({self.number})"

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances from list1 that match any instance in list2
for item in list2:
    if item in list1:
        list1.remove(item)

print(list1)  # Output: [Move(1), Move(2), Move(4)]
