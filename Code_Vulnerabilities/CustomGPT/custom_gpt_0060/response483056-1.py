
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    f = 1  # This will control the direction of sorting

    while start < end:
        if f == 1:
            for i in range(start, end):
                if aList[i] > aList[i + 1]:
                    aList[i], aList[i + 1] = aList[i + 1], aList[i]

            end -= 1
            f = -1  # Change direction for next pass

        else:  # f == -1
            for i in range(end, start, -1):
                if aList[i] < aList[i - 1]:
                    aList[i], aList[i - 1] = aList[i - 1], aList[i]

            start += 1
            f = 1  # Change direction for next pass

# Example usage:
aList = [5, 2, 3, 6, 1]
cocktail_sort(aList)
print(aList)  # Output will be the sorted list: [1, 2, 3, 5, 6]
