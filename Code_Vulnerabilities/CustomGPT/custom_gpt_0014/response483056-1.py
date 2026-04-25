
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    swapped = True
    f = 1  # Direction: 1 for left to right, -1 for right to left

    while swapped:
        swapped = False

        # Left to right pass
        if f == 1:
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    # Swap elements
                    area[i], area[i + 1] = area[i + 1], area[i]
                    swapped = True

            end -= 1
        else:  # Right to left pass
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    # Swap elements
                    area[i], area[i - 1] = area[i - 1], area[i]
                    swapped = True

            start += 1

        f = -f  # Alternate direction

    return area

# Example Usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
