
from itertools import product

# Your list of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# Generating tuples using itertools.product and filtering with a comprehension
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if i + j + k == 0]

# Output the result
print(result)
