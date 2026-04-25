
from itertools import product

# Given list
numbers = [-4, -2, 1, 2, 5, 0]

# Generate tuples and filter those whose sum is zero
result = [t for t in product(numbers, repeat=3) if sum(t) == 0]

print(result)
