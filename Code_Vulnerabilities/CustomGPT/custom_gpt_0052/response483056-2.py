
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

        end -= 1

        if not swapped:
            break

        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Swap
                swapped = True

        start += 1

    return arr

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print("Sorted List:", sorted_list)
