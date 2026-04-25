
aList = [5, 2, 3, 6, 1]

for i in range(len(aList) - 1):
    if aList[i] > aList[i + 1]:
        aList[i], aList[i + 1] = aList[i + 1], aList[i]

print("Sorted list:", aList)
