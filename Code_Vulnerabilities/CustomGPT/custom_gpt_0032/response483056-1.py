
aList = [5, 2, 3, 6, 1]
start, end = 0, len(aList)

for item in aList[start:end]:
    aList[aList.index(item)], aList[aList.index(item) + 1] = aList[aList.index(item)], aList[aList.index(item) + 1]
