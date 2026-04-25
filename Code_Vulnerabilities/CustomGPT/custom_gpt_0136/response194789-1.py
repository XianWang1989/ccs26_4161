
import itertools

def foo(numbers):
    # Create a list of tuples where each number can be either positive or negative
    options = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations of the options using itertools.product
    result = list(itertools.product(*options))

    return result

# Example usages
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # [[1, -1, 1], [-1, -1, 1], ...]
