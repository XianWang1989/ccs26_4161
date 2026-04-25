
from itertools import product

# Define the list
numbers = [-4, -2, 1, 2, 5, 0]

# Use itertools.product to generate all combinations of three elements
result = [
    (i, j, k) for i, j, k in product(numbers, repeat=3) if sum((i, j, k)) == 0
]

# Print the result
print(result)
