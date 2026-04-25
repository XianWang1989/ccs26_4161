
class move(object):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, move):
            return self.number == other.number
        return False

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove instances from list1 that have the same number as any instance in list2
for item in list2:
    list1 = [x for x in list1 if x.number != item.number]

# Result
for item in list1:
    print(item.number)  # This will print: 1, 2, 4
