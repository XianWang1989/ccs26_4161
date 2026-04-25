
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap
                swapped = True

        # If nothing has moved, then the array is sorted
        if not swapped:
            break

        # Move the end pointer back
        end -= 1
        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Swap
                swapped = True

        # Move the start pointer forward
        start += 1

# Example usage:
aList = [5, 2, 3, 6, 1]
print("Original List:", aList)
cocktail_sort(aList)
print("Sorted List:", aList)
