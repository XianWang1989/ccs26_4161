
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Traverse the list forward
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        end -= 1

        # Traverse the list backward
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start += 1

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output will be sorted list: [1, 2, 3, 5, 6]
