
def foo(numbers):
    if not numbers:
        return [[]]  # Base case: return a list with an empty list

    # Recursive case
    first = numbers[0]
    rest = numbers[1:]

    # Generate possibilities for the rest of the numbers
    possibilities = foo(rest)

    # Combine the first number's two possibilities with each of the combinations of the rest
    with_positive = [[abs(first)] + possibility for possibility in possibilities]
    with_negative = [[-abs(first)] + possibility for possibility in possibilities]

    return with_positive + with_negative

# Example usages:
print(foo([-4]))  # [[4], [-4]]
print(foo([1, 1]))  # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, -1, 1], [-1, 1, 1], [-1, 1, -1]]
