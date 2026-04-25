
from itertools import product

# Input list
numbers = [-4, -2, 1, 2, 5, 0]

# Generate tuples and filter by the sum condition
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if sum((i, j, k)) == 0]

# Output the result
print(result)
