class move(object):
    def __init__(self, number):
        self.number = number

list1 = [move(1), move(2), move(3), move(4)]
list2 = [move(3), move(7)]

# Remove items from list1 that have the same 'number' attribute as any in list2
for item2 in list2:
    list1 = [item1 for item1 in list1 if item1.number != item2.number]

# To verify the result
for item in list1:
    print(item.number)
