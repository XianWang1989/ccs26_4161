
from itertools import product

# List of elements
elements = [-4, -2, 1, 2, 5, 0]

# Generate tuples and filter those that sum to zero
result = [t for t in product(elements, repeat=3) if sum(t) == 0]

print(result)
