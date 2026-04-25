
def foo(numbers):
    from itertools import product

    # Create a list of '+' and '-' options for each number
    options = [tuple((abs(num), -abs(num))) for num in numbers]

    # Generate all combinations
    combinations = list(product(*options))

    return [list(combination) for combination in combinations]

# Example usage:
print(foo([-4]))  # [[4], [-4]]
print(foo([1, 1]))  # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
