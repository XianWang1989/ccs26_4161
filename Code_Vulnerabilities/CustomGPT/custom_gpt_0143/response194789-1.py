
def foo(lst):
    if not lst:
        return [[]]

    first = lst[0]
    rest = foo(lst[1:])

    positive_first = abs(first)
    negative_first = -abs(first)

    result = []

    for combination in rest:
        result.append([positive_first] + combination)
        result.append([negative_first] + combination)

    return result

# Example usage:
print(foo([-4]))
print(foo([1, 1]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
