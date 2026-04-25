
# Cocktail Sort Implementation
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    f = 1  # direction flag

    while start < end:

        if f == 1:  # Moving right to left
            for i in range(start, end):
                if aList[i] > aList[i + 1]:
                    # Swap
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]
            end -= 1  # Reduce the end pointer
        else:  # Moving left to right
            for i in range(end, start, -1):
                if aList[i] < aList[i - 1]:
                    # Swap
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]
            start += 1  # Increase the start pointer

        f = ~f + 1  # Toggle direction

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output will be [1, 2, 3, 5, 6]
