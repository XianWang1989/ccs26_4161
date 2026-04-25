
def cocktail_sort(aList):
    n = len(aList)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Traverse from left to right
        for i in range(start, end):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]  # Swap
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # Traverse from right to left
        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                aList[i], aList[i - 1] = aList[i - 1], aList[i]  # Swap
                swapped = True

        start += 1

# Example usage
my_list = [5, 2, 3, 6, 1]
cocktail_sort(my_list)
print(my_list)  # Output: [1, 2, 3, 5, 6]
