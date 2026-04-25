
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Traverse the list from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:  # If the current element is greater than the next
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap them
                swapped = True

        # If nothing was swapped, then the array is sorted
        if not swapped:
            break

        # Move the end pointer backward
        end -= 1
        swapped = False

        # Traverse the list from right to left
        for i in range(end, start - 1, -1):
            if arr[i] < arr[i - 1]:  # If the current element is less than the previous
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Swap them
                swapped = True

        # Move the start pointer forward
        start += 1

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output: [1, 2, 3, 5, 6]
