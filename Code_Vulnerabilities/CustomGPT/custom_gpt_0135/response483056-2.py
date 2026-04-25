
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1

    while start < end:
        if f == 1:  # Forward pass
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    # Swap if the current item is greater than the next
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1  # Reduce the end index after sorting
        else:  # Backward pass
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    # Swap if the current item is less than the previous
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1  # Increase the start index after sorting

        f = -f  # Toggle the direction

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)
