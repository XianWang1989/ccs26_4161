
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    f = 1

    while start < end:
        if f == 1:
            for i in range(start, end):
                if aList[i] > aList[i + 1]:
                    # Swap elements
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]
            end -= 1
            f = -1

        else:  # f == -1
            for i in range(end, start, -1):
                if aList[i] < aList[i - 1]:
                    # Swap elements
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]
            start += 1
            f = 1

    return aList

# Example usage
print(cocktail_sort([5, 2, 3, 6, 1]))
