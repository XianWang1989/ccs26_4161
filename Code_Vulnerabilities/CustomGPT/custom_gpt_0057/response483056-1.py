
def cocktail_sort(aList):
    start = 0
    end = len(aList) - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(start, end):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True
        end -= 1

        for i in range(end, start, -1):
            if aList[i] < aList[i - 1]:
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
                swapped = True
        start += 1

    return aList

aList = [5, 2, 3, 6, 1]
sorted_list = cocktail_sort(aList)
print(sorted_list)
