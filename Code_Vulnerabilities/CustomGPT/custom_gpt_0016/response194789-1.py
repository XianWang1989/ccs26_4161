
def foo(numbers):
    if not numbers:
        return [[]]  # Return a list containing an empty list when the input is empty

    # Get the first number and the rest of the numbers
    first = numbers[0]
    rest = numbers[1:]

    # Generate possibilities for the rest of the numbers
    rest_possibilities = foo(rest)

    # Create a new list to store the combinations
    combinations = []

    # Loop through rest combinations and add current possibilities
    for possibility in rest_possibilities:
        # Adding both positive and negative first number possibility
        combinations.append([abs(first)] + possibility)
        combinations.append([-abs(first)] + possibility)

    return combinations

# Test cases
print(foo([-4]))                   # Output: [[4], [-4]]
print(foo([1, 1]))                 # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))             # Output: [[1, -1, 1], [1, -1, -1], [1, 1, 1], [1, 1, -1], [-1, -1, 1], [-1, -1, -1], [-1, 1, 1], [-1, 1, -1]]
