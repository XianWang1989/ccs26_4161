
from itertools import product

numbers = [-4, -2, 1, 2, 5, 0]
result = [tuple(p) for p in product(numbers, repeat=3) if sum(p) == 0]

print(result)
