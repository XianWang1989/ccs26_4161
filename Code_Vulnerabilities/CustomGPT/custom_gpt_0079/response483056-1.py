
def cocktail_sort(area):
    start, end = 0, len(area) - 1
    f = 1  # Direction flag

    while start < end:
        if f == 1:  # Forward pass
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    # Swap elements
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1  # Decrease end index

        else:  # Backward pass
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    # Swap elements
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1  # Increase start index

        f = ~f + 1  # Toggle direction

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)  # Output: [1, 2, 3, 5, 6]
