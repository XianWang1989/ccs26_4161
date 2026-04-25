
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1  # Direction flag

    while start < end:
        if f == 1:
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    # Swap the elements
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1  # Reduce end point as the last element is sorted
        else:
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    # Swap the elements
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1  # Increase start point as the first element is sorted

        f = -f  # Change direction

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sortedList = cocktail_sort(aList)
print(sortedList)  # Output: [1, 2, 3, 5, 6]
