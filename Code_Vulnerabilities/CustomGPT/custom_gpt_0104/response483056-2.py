
def cocktail_sort(array):
    start = 0
    end = len(array) - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Swap
                swapped = True

        if not swapped:
            break  # If no elements were swapped, we're done

        # Reduce end boundary since the last element is in place
        end -= 1
        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]  # Swap
                swapped = True

        # Increase start boundary since the first element is in place
        start += 1

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output will be [1, 2, 3, 5, 6]
