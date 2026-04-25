
def cocktail_sort(lst):
    start = 0
    end = len(lst) - 1
    swapped = True

    while swapped:
        swapped = False
        # Forward pass
        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

        # If no elements were swapped, the list is sorted
        if not swapped:
            break

        # Reduce the end index
        end -= 1

        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                swapped = True

        # Increase the start index
        start += 1

    return lst

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)  # Output: [1, 2, 3, 5, 6]
