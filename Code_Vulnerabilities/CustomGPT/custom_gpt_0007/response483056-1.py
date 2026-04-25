
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1  # 1 for left-to-right, -1 for right-to-left

    while start < end:
        if f == 1:
            for i in range(start, end):
                print(area, f, area[i], area[i+1])
                if area[i] > area[i + 1]:
                    # Swap elements
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1
            f = -1  # Switch direction

        elif f == -1:
            for i in range(end, start, -1):
                print(area, f, area[i], area[i-1])
                if area[i] < area[i - 1]:
                    # Swap elements
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1
            f = 1  # Switch direction

    return area

# Example usage:
area = [5, 2, 3, 6, 1]
sorted_area = cocktail_sort(area)
print("Sorted Area:", sorted_area)
