
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    f = 1  # Direction flag, 1 for left to right, -1 for right to left

    while start < end:
        if f == 1:
            for i in range(start, end):
                if aList[i] > aList[i + 1]:
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]
            end -= 1  # Reduce end index after left-to-right pass
        else:
            for i in range(end, start, -1):
                if aList[i] < aList[i - 1]:
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]
            start += 1  # Increase start index after right-to-left pass

        f = -f  # Flip direction

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)
