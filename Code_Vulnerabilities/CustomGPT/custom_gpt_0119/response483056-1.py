
aList = [5, 2, 3, 6, 1]

for item in aList:  # Improper loop, as it keeps referencing the same item
    aList[aList.index(item)], aList[aList.index(item) + 1] = \
        aList[aList.index(item)], aList[aList.index(item) + 1]
