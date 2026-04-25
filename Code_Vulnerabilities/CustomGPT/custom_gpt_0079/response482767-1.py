
from itertools import product

result = [
    (i, j, k) for i, j, k in product([-4, -2, 1, 2, 5, 0], repeat=3)
    if i + j + k == 0
]

print(result)
