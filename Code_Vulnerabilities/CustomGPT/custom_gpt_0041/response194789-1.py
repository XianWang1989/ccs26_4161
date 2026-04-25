
def foo(numbers):
    if not numbers:
        return [[]]  # Base case: return a list containing an empty list

    # Get the first number and the rest of the list
    first = abs(numbers[0])  # Use absolute value to ensure positivity
    rest = numbers[1:]  # The rest of the list

    # Recursively get combinations of the rest of the list
    rest_combinations = foo(rest)

    # Create new combinations by adding the current number's positive and negative
    combinations = []
    for combination in rest_combinations:
        combinations.append([first] + combination)    # Positive
        combinations.append([-first] + combination)   # Negative

    return combinations

# Example usage:
print(foo([-4]))                 # Output: [[4], [-4]]
print(foo([1, 1]))              # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # Output: [[1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1], [1, 1, -1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1]]
