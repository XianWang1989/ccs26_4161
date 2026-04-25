
from itertools import product

# List of values
values = [-4, -2, 1, 2, 5, 0]

# Generate tuples and filter by sum
result = [(i, j, k) for i, j, k in product(values, repeat=3) if sum((i, j, k)) == 0]

print(result)
