
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1  # Sort direction indicator

    while start <= end:
        if f == 1:
            for i in range(start, end):
                # Compare adjacent elements
                if area[i] > area[i + 1]:
                    area[i], area[i + 1] = area[i + 1], area[i]  # Swap
            end -= 1
        else:
            for i in range(end, start, -1):
                # Compare adjacent elements
                if area[i] < area[i - 1]:
                    area[i], area[i - 1] = area[i - 1], area[i]  # Swap
            start += 1
        f *= -1  # Change direction

    return area


# Example usage
area = [5, 2, 3, 6, 1]
sorted_area = cocktail_sort(area)
print(sorted_area)  # Output: [1, 2, 3, 5, 6]
