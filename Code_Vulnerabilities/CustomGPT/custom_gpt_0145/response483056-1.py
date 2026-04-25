
# Correct way to swap adjacent elements in a list
aList = [5, 2, 3, 6, 1]

# Using a range to loop through indices
for i in range(len(aList) - 1):
    if aList[i] > aList[i + 1]:
        # Swap elements
        aList[i], aList[i + 1] = aList[i + 1], aList[i]

print(aList)  # Output will be [2, 3, 5, 6, 1]
