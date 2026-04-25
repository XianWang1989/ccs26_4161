
from itertools import product

# Your list of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# Generating tuples and filtering based on the sum
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if sum((i, j, k)) == 0]

print(result)
