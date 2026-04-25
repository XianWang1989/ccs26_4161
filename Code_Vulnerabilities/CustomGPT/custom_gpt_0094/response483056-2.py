
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1  # Forward flag

    while start < end:
        if f == 1:
            for i in range(start, end):
                if area[i] > area[i + 1]:
                    area[i], area[i + 1] = area[i + 1], area[i]
            end -= 1
        else:
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:
                    area[i], area[i - 1] = area[i - 1], area[i]
            start += 1
        f = -f  # Toggle direction

    return area

# Example usage
aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)
