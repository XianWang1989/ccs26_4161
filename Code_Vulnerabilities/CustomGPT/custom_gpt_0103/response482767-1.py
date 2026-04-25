
from itertools import product

# Define the list
numbers = [-4, -2, 1, 2, 5, 0]

# Use product to generate tuples and filter based on the sum
result = [t for t in product(numbers, repeat=3) if sum(t) == 0]

print(result)
