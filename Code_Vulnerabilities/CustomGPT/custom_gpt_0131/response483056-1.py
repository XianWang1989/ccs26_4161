
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    swapped = True

    while swapped:
        # Reset the swapped flag on each pass
        swapped = False

        # Forward pass
        for i in range(start, end):
            if aList[i] > aList[i + 1]:
                # Swap elements
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True

        # If no swaps were made, the list is sorted
        if not swapped:
            break

        # Decrease end because the last element is in place
        end -= 1

        # Backward pass
        swapped = False
        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                # Swap elements
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
                swapped = True

        # Increase start because the first element is in place
        start += 1

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output will be [1, 2, 3, 5, 6]
