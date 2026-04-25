
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    swapped = True  # To make sure we are in the loop

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if aList[i] > aList[i + 1]:
                # Swap elements
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True

        end -= 1  # Reduce the endpoint

        # Backward pass
        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                # Swap elements
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
                swapped = True

        start += 1  # Increase the startpoint

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output should be the sorted list: [1, 2, 3, 5, 6]
