
from itertools import product

def foo(lst):
    # Create a list of lists with both positive and negative values
    possibilities = [[abs(num), -abs(num)] for num in lst]

    # Generate all combinations of the possibilities using product
    result = list(product(*possibilities))

    return result

# Example usage:
print(foo([-4]))                      # [[4], [-4]]
print(foo([1, 1]))                   # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                  # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))                # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [...] 

# Testing with mixture of signs
print(foo([1, -1, 1]))               # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ... ]
