
from itertools import product

def foo(numbers):
    # Create a list of positive and negative possibilities
    possibilities = [[abs(num) if num >= 0 else -abs(num) for num in numbers]]
    signs = [[1 if num >= 0 else -1 for num in numbers]]

    # Generate all combinations of signs (+/-)
    combinations = product(*[[sign, -sign] for sign in signs[0]])

    # Build the resulting list of lists
    result = [[abs(num) * sign for num, sign in zip(numbers, combo)] for combo in combinations]

    return result

# Example usage
print(foo([-4]))
print(foo([1, 1]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
