
def cocktail_sort(array):
    start = 0
    end = len(array) - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if array[i] > array[i + 1]:  # swap if current is greater than next
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        end -= 1

        if not swapped:
            break

        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if array[i] < array[i - 1]:  # swap if current is less than previous
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

        start += 1

    return array

# Example usage:
if __name__ == "__main__":
    aList = [5, 2, 3, 6, 1]
    sortedList = cocktail_sort(aList)
    print(sortedList)  # Output: [1, 2, 3, 5, 6]
