
from itertools import product

lst = [-4, -2, 1, 2, 5, 0]

# Using itertools.product to generate tuples
result = [t for t in product(lst, repeat=3) if sum(t) == 0]

print(result)
