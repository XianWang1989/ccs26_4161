
from itertools import product

# Sample list
numbers = [-4, -2, 1, 2, 5, 0]

# Generate three-element tuples and filter based on the sum condition
result = [
    (i, j, k) for i, j, k in product(numbers, repeat=3) if sum((i, j, k)) == 0
]

print(result)
