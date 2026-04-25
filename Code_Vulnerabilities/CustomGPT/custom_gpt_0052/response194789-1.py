
def foo(numbers):
    if not numbers:
        return [[]]

    first = numbers[0]
    rest = numbers[1:]

    # Generate possibilities for the rest of the numbers
    rest_possibilities = foo(rest)

    # Create current possibilities by adding both + and - of the first number
    current_possibilities = []
    for possibility in rest_possibilities:
        current_possibilities.append([abs(first)] + possibility)  # Positive
        current_possibilities.append([-abs(first)] + possibility)  # Negative

    return current_possibilities

# Test cases
print(foo([-4]))          # Output: [[4], [-4]]
print(foo([1, 1]))       # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]

