
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    sorted = False

    while not sorted:
        sorted = True

        # Forward pass
        for i in range(start, end):
            if area[i] > area[i + 1]:
                area[i], area[i + 1] = area[i + 1], area[i]
                sorted = False

        end -= 1

        # Backward pass
        for i in range(end, start, -1):
            if area[i] < area[i - 1]:
                area[i], area[i - 1] = area[i - 1], area[i]
                sorted = False

        start += 1

    return area

# Example usage
area = [5, 2, 3, 6, 1]
sorted_area = cocktail_sort(area)
print(sorted_area)  # Output: [1, 2, 3, 5, 6]
