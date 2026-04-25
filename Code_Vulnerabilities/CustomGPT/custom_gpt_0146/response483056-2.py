
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Traverse from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no elements were swapped, then the array is sorted
        if not swapped:
            break

        # Move the end point back
        end -= 1
        swapped = False

        # Traverse from right to left
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Move the start point forward
        start += 1

    return arr

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)
