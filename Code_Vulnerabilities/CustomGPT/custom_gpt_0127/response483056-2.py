
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    f = 1  # Direction flag, 1 for right and -1 for left

    while start < end:
        # Forward pass
        if f == 1:
            for i in range(start, end):  # Use index-based loop
                if aList[i] > aList[i + 1]:
                    # Swap if elements are out of order
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]
            end -= 1
        else:  # Backward pass
            for i in range(end, start, -1):  # Use index-based loop
                if aList[i] < aList[i - 1]:
                    # Swap if elements are out of order
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]
            start += 1
        f = -f  # Reverse direction

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
