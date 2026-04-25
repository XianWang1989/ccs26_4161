
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if area[i] > area[i + 1]:
                area[i], area[i + 1] = area[i + 1], area[i]
                swapped = True

        end -= 1

        # Backward pass
        if not swapped:
            break

        swapped = False

        for i in range(end, start, -1):
            if area[i] < area[i - 1]:
                area[i], area[i - 1] = area[i - 1], area[i]
                swapped = True

        start += 1

area = [5, 2, 3, 6, 1]
cocktail_sort(area)
print(area)
