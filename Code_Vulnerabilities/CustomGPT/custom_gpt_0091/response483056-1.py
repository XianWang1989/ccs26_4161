
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    f = 1  # Direction flag

    while start < end:
        if f == 1:  # Forward pass
            for i in range(start, end):
                if aList[i] > aList[i + 1]:
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]  # Swap
            end -= 1
        else:  # Backward pass
            for i in range(end, start, -1):
                if aList[i] < aList[i - 1]:
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]  # Swap
            start += 1
        f *= -1  # Change direction

    return aList

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
