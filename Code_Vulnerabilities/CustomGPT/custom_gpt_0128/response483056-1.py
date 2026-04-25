
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    f = 1  # Direction of sorting

    while start < end:
        if f == 1:  # Left to right
            for i in range(start, end):
                print(arr, f, i, arr[i+1])
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            end -= 1
        else:  # Right to left
            for i in range(end, start, -1):
                print(arr, f, i, arr[i-1])
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            start += 1
        f = -f  # Toggle direction

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)
