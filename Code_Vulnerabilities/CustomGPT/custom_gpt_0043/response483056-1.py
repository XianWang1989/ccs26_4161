
def cocktail_sort(area):
    start = 0
    end = len(area) - 1
    f = 1  # Forward direction

    while start < end:
        if f == 1:  # Forward pass
            swapped = False
            for i in range(start, end):
                if area[i] > area[i + 1]:  # Compare adjacent elements
                    # Swap if they are in the wrong order
                    area[i], area[i + 1] = area[i + 1], area[i]
                    swapped = True
            end -= 1  # Reduce the end boundary
            f = -1  # Change direction

        elif f == -1:  # Backward pass
            swapped = False
            for i in range(end, start, -1):
                if area[i] < area[i - 1]:  # Compare adjacent elements
                    # Swap if they are in the wrong order
                    area[i], area[i - 1] = area[i - 1], area[i]
                    swapped = True
            start += 1  # Increase the start boundary
            f = 1  # Change direction

        if not swapped:  # If no elements were swapped, the list is sorted
            break

# Example usage
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output will be a sorted list
