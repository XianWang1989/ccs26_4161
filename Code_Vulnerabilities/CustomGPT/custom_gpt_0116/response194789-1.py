
import itertools

def foo(numbers):
    # Create lists of potential positive and negative values
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations of these possibilities
    result = list(itertools.product(*possibilities))

    return result

# Example usages
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 2]))       # [[1, 2], [1, -2], [-1, 2], [-1, -2]]
print(foo([3, -1]))      # [[3, 1], [3, -1], [-3, 1], [-3, -1]]
print(foo([1, -2, 3]))   # [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3], [-1, -2, -3]]
