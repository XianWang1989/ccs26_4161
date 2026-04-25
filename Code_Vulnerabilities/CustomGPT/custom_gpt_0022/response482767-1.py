
from itertools import product

# Define the list
numbers = [-4, -2, 1, 2, 5, 0]

# Generate tuples with a comprehension and filter by the sum condition
result = [tup for tup in product(numbers, repeat=3) if sum(tup) == 0]

print(result)
