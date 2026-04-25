
from itertools import product

# List of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# Generating tuples with sum equal to 0
result = [tup for tup in product(numbers, repeat=3) if sum(tup) == 0]

print(result)
