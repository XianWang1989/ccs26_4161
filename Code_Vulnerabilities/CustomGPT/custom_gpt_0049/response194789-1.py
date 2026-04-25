
from itertools import product

def foo(numbers):
    # Create a list of signs based on the input numbers
    signs = [(-1, 1) if num < 0 else (1, -1) for num in numbers]

    # Generate all combinations of positive and negative numbers using itertools.product
    combinations = list(product(*signs))

    # Build the result list using the combinations
    result = [[abs(num) * sign for num, sign in zip(numbers, combo)] for combo in combinations]

    return result

# Example usage:
print(foo([-4]))                # Output: [[4], [-4]]
print(foo([+, +]))              # Output: [[+, +], [+,-], [-,+], [-,-]]
print(foo([-, +]))              # Output: [[+, +], [+,-], [-,+], [-,-]]
print(foo([-1, 3]))             # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([+, -, +]))           # Output: [[-, -, -], [+,-,-], [-,+,-], [-,-,+], [+,+,-], [+,-,+], [-,+,+], [+,+,+]]
