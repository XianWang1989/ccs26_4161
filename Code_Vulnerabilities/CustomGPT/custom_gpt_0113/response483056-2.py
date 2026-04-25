
def cocktail_sort(aList):
    n = len(aList)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False
        # Forward direction
        for i in range(start, end):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True
        end -= 1

        # If no elements were swapped, the list is sorted
        if not swapped:
            break

        swapped = False
        # Backward direction
        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
                swapped = True
        start += 1

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
