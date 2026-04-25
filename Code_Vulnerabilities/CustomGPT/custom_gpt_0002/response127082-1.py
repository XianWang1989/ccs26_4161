
class Move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number

list1 = [Move(1), Move(2), Move(3), Move(4)]
list2 = [Move(3), Move(7)]

# Remove instances in list1 with the same number as those in list2
list1 = [item for item in list1 if item not in list2]

print([item.number for item in list1])  # Output: [1, 2, 4]
