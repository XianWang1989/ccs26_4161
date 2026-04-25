
from itertools import product

# List of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# Generating tuples with the condition
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if sum([i, j, k]) == 0]

print(result)
