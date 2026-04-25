
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    swapped = True
    f = 1  # Direction: 1 for forward, -1 for backward

    while swapped:
        swapped = False

        if f == 1:
            for i in range(start, end):
                if aList[i] > aList[i + 1]:
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]  # Swap
                    swapped = True
            end -= 1  # Reduce end after each forward pass
        else:
            for i in range(end, start, -1):
                if aList[i] < aList[i - 1]:
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]  # Swap
                    swapped = True
            start += 1  # Increase start after each backward pass

        f = -f  # Change direction
    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)  # Output will be a sorted list
