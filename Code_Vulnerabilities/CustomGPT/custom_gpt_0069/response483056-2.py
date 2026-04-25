
aList = [5, 2, 3, 6, 1]
start = 0
end = len(aList)

for i in range(start, end - 1):
    if aList[i] > aList[i + 1]:
        # Swap elements
        aList[i], aList[i + 1] = aList[i + 1], aList[i]

print(aList)
