
aList = [5, 2, 3, 6, 1]
for item in aList[0:5]:
    aList[aList.index(item)], aList[aList.index(item) + 1] = aList[aList.index(item)], aList[aList.index(item) + 1]
