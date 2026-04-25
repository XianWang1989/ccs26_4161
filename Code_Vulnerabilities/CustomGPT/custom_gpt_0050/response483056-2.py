
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    f = 1

    while start < end:
        if f == 1:  # Moving forward
            for i in range(start, end):
                print(aList, f, i, aList[i + 1], i + 1)
                if aList[i] > aList[i + 1]:
                    # Swap directly using the index
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]
            end -= 1
        else:  # Moving backward
            for i in range(end, start, -1):
                print(aList, f, i, aList[i - 1], i - 1)
                if aList[i] < aList[i - 1]:
                    # Swap directly using the index
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]
            start += 1
        f = -f  # Toggle direction

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)
