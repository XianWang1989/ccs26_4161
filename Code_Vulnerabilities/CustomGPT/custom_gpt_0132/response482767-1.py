
from itertools import product

nums = [-4, -2, 1, 2, 5, 0]
tuples = [(i, j, k) for i, j, k in product(nums, repeat=3) if sum((i, j, k)) == 0]

print(tuples)
