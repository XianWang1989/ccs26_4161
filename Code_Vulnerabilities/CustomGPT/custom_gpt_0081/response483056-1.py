
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                # Swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If nothing was swapped, then the list is sorted
        if not swapped:
            break

        swapped = False
        end -= 1

        # Backward pass
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                # Swap elements
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start += 1

    return arr

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list) # Output: [1, 2, 3, 5, 6]
