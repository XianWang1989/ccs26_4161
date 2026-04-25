
class move(object):
    def __init__(self, number):
        self.number = number

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

for item in list2:
    # Use a list comprehension to filter out the items
    list1 = [m for m in list1 if m.number != item.number]

# Now, list1 will only contain instances that are not in list2
print([m.number for m in list1])  # Output: [1, 2, 4]
