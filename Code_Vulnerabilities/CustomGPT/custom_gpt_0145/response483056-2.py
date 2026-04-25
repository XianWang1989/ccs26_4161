
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1

    while start < end:
        if f == 1:  # Forward pass
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    # Swap elements
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1  # Reduce the end boundary
        else:  # Backward pass
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    # Swap elements
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1  # Increase the start boundary

        f = -f  # Toggle direction

    return area

# Example usage
area = [5, 2, 3, 6, 1]
sorted_area = cocktail_sort(area)
print(sorted_area)  # Output will be [1, 2, 3, 5, 6]
