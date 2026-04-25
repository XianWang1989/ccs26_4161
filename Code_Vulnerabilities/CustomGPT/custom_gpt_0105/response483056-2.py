
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

        if not swapped:
            break

        end -= 1
        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
                swapped = True

        start += 1

# Example Usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output: [1, 2, 3, 5, 6]
