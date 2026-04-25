
from itertools import product

elements = [-4, -2, 1, 2, 5, 0]

result = [
    (i, j, k) for i, j, k in product(elements, repeat=3) if sum((i, j, k)) == 0
]

print(result)
