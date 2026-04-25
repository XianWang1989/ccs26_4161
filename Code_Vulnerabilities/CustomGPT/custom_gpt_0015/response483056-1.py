
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    f = 1  # Direction flag (1 for left to right, -1 for right to left)

    while start < end:
        if f == 1:
            for i in range(start, end):
                print(arr, f, i, i + 1)
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            end -= 1
            f = -1
        else:
            for i in range(end, start, -1):
                print(arr, f, i, i - 1)
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            start += 1
            f = 1

    return arr

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print("Sorted List:", sorted_list)
