
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1  # direction, 1 for left-to-right, -1 for right-to-left

    while start < end:
        if f == 1:
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    # Swap using direct indexing
                    area[i], area[i + 1] = area[i + 1], area[i]

            end -= 1
            f = -1  # Change direction to right-to-left

        else:
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    # Swap using direct indexing
                    area[i], area[i - 1] = area[i - 1], area[i]

            start += 1
            f = 1  # Change direction to left-to-right

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)
