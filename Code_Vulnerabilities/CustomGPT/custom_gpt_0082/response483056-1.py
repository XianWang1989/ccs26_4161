
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    swapped = True

    while swapped:
        swapped = False
        # Forward pass
        for i in range(start, end):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True

        # If nothing was swapped, then the list is sorted
        if not swapped:
            break

        # Reduce the end index
        end -= 1
        swapped = False

        # Backward pass
        for i in range(end, start - 1, -1):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True

        # Increase the start index
        start += 1

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)  # Output: [1, 2, 3, 5, 6]
