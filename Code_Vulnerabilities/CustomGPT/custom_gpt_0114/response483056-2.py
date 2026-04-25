
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Traverse through the array from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements
                swapped = True

        # If nothing moved, then array is sorted
        if not swapped:
            break

        # Otherwise, reset the swapped flag so we can check again
        swapped = False
        end -= 1  # Move the end because last element is sorted

        # Traverse through the array from right to left
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Swap elements
                swapped = True

        start += 1  # Move the start because first element is sorted

    return arr

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
