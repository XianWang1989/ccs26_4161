
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

        end -= 1  # Decrease end since the last item is sorted

        # Backward pass
        if not swapped:
            break  # If no elements were swapped, the list is sorted
        swapped = False

        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
                swapped = True

        start += 1  # Increase start since the first item is sorted

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)
