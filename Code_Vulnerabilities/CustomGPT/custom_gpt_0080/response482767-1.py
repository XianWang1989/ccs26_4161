
from itertools import product

# Given list
numbers = [-4, -2, 1, 2, 5, 0]

# Generate three-element tuples where the sum is zero
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if sum((i, j, k)) == 0]

# Output the result
print(result)
