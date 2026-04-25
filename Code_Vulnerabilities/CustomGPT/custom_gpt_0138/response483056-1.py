
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    swapping = True

    while swapping:
        swapping = False

        # Forward pass
        for i in range(start, end):
            if area[i] > area[i + 1]:
                area[i], area[i + 1] = area[i + 1], area[i]
                swapping = True

        end -= 1  # Decrease the end index as the last element is sorted

        # Backward pass
        for i in range(end, start, -1):
            if area[i] < area[i - 1]:
                area[i], area[i - 1] = area[i - 1], area[i]
                swapping = True

        start += 1  # Increase the start index as the first element is sorted

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)
