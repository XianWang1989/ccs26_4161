
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True
    f = 1  # Direction: +1 for forward, -1 for backward

    while swapped:
        swapped = False

        # Forward pass
        if f == 1:
            for i in range(start, end):
                print(f"Comparing {arr[i]} and {arr[i+1]}")
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            end -= 1
        else:  # Backward pass
            for i in range(end, start, -1):
                print(f"Comparing {arr[i]} and {arr[i-1]}")
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swapped = True
            start += 1

        # Change direction
        f = -f

    return arr

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print("Sorted list:", sorted_list)
