
from itertools import product

def foo(numbers):
    # Generate all combinations of '+' and '-' for each number
    possibilities = list(product(*[(abs(num), -abs(num)) for num in numbers]))
    return possibilities

# Example usage
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1]))           # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([1, -2, 3]))        # [[1, -2, 3], [1, -2, -3], [1, 2, 3], ..., [-1, 2, -3]]
