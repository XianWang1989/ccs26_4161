
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1

    while start < end:
        if f == 1:  # Forward pass
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    # Swap using tuple unpacking
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1
        else:  # Backward pass
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    # Swap using tuple unpacking
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1

        f *= -1  # Toggle direction

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)  # Output: [1, 2, 3, 5, 6]
