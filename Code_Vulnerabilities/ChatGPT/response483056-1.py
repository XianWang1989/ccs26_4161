
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True
    f = 1  # Direction flag

    while swapped:
        swapped = False

        # Forward pass
        if f == 1:
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    # Swap elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            end -= 1

        # Backward pass
        else:
            for i in range(end, start, -1):
                if arr[i] < arr[i - 1]:
                    # Swap elements
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swapped = True
            start += 1

        f = -f  # Switch direction

    return arr

# Example usage:
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)  # Output: [1, 2, 3, 5, 6]
