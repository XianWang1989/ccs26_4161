
import itertools

def foo(numbers):
    # Generate tuples of (positive, negative) for each number
    options = [[num, -num] for num in numbers]
    # Create a Cartesian product of all options
    results = list(itertools.product(*options))
    # Convert tuples to lists
    return [list(result) for result in results]

# Example usage
print(foo([-4]))         # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))   # [[-1, -1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, 1], [-1, -1, -1], [-1, 1, -1], [1, -1, -1], [1, 1, -1]]
