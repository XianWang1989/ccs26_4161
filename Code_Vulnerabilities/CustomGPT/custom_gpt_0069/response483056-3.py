
def cocktail_sort(area):
    start = 0
    end = len(area)
    f = 1

    while start < end:
        if f == 1:
            for i in range(start, end - 1):
                if area[i] > area[i + 1]:
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1

        else:
            for i in range(end - 1, start, -1):
                if area[i] < area[i - 1]:
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1

        f *= -1  # Toggle direction

    return area

# Example usage
area = [5, 2, 3, 6, 1]
sorted_area = cocktail_sort(area)
print(sorted_area)
