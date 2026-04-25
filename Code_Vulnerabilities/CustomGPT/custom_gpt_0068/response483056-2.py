
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    swapped = True

    while swapped:
        # reset the swapped flag on entering the loop, because it might be true from a previous iteration
        swapped = False

        # Forward pass
        for i in range(start, end):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True

        end -= 1

        # If nothing was swapped, the list is sorted
        if not swapped:
            break

        # Backward pass
        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
                swapped = True

        start += 1

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output: [1, 2, 3, 5, 6]
