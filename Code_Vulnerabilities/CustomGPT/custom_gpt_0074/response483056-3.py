
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1

    while start < end:
        if f == 1:  # Forward pass
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    area[i], area[i + 1] = area[i + 1], area[i]  # Swap
            end -= 1
            f = -1  # Change direction

        else:  # Backward pass
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    area[i], area[i - 1] = area[i - 1], area[i]  # Swap
            start += 1
            f = 1  # Change direction

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)
