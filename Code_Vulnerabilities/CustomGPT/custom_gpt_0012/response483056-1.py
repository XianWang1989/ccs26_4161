
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1  # direction flag, 1 for right, -1 for left

    while start < end:
        if f == 1:  # Going right
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    area[i], area[i + 1] = area[i + 1], area[i]  # Swap
            end -= 1  # Reduce the range for the next pass
        else:  # Going left
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    area[i], area[i - 1] = area[i - 1], area[i]  # Swap
            start += 1  # Reduce the range for the next pass
        f = -f  # Flip the direction flag

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
