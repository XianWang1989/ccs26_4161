
def cocktail_sort(arr):
    n = len(arr)
    swapped = True

    # Loop until no swaps are made
    while swapped:
        swapped = False

        # Forward pass
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        # Reduce the end index
        n -= 1

        swapped = False

        # Backward pass
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Increase the start index
        start += 1

    return arr

# Example usage:
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
