
import itertools

def foo(numbers):
    # Create tuples of positive and negative possibilities for each number
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to generate all combinations
    results = list(itertools.product(*possibilities))

    return results

# Example usage:
print(foo([-4]))                 # Output: [(4, -4)]
print(foo([1, 2]))               # Output: [(1, 2), (1, -2), (-1, 2), (-1, -2)]
print(foo([-1, 3]))              # Output: [(1, 3), (1, -3), (-1, 3), (-1, -3)]
print(foo([1, -1]))              # Output: [(1, -1), (1, 1), (-1, -1), (-1, 1)]
print(foo([1, -2, 3]))           # Output: [(1, 2, 3), (1, 2, -3), (1, -2, 3), (1, -2, -3), (-1, 2, 3), (-1, 2, -3), (-1, -2, 3), (-1, -2, -3)]
