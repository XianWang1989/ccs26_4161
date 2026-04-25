
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if area[i] > area[i + 1]:
                area[i], area[i + 1] = area[i + 1], area[i]  # Swap
                swapped = True

        # If nothing was swapped, the array is sorted
        if not swapped:
            break

        # Move the end point back
        end -= 1

        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if area[i] < area[i - 1]:
                area[i], area[i - 1] = area[i - 1], area[i]  # Swap
                swapped = True

        # Move the start point forward
        start += 1

    return area

# Example usage:
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
