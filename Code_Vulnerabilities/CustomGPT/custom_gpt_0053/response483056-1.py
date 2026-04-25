
aList = [5, 2, 3, 6, 1]

for item in aList:
    aList[aList.index(item)], aList[aList.index(item) + 1] = aList[aList.index(item)], aList[aList.index(item) + 1]
