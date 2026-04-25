
import itertools

def foo(numbers):
    # Create a list of tuples with positive and negative versions of each number
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Use itertools.product to generate all combinations
    results = list(itertools.product(*possibilities))

    return results

# Example usage
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ... ]
