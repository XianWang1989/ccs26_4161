aList = [5, 2, 3, 6, 1]

for item in aList[0:4]:  # effectively [5,2,3,6]
    print("Current list:", aList)
    i = aList.index(item)
    print(f"Swapping index {i} and {i+1} -> {aList[i]} <-> {aList[i+1]}")
    aList[i], aList[i+1] = aList[i+1], aList[i]
