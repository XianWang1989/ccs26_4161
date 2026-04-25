
from itertools import product

# Define the list
numbers = [-4, -2, 1, 2, 5, 0]

# Generate all combinations of three elements and filter those with a sum of zero
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if i + j + k == 0]

# Output the result
print(result)
