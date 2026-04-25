
from itertools import combinations_with_replacement

elements = [-4, -2, 1, 2, 5, 0]
tuples = [(i, j, k) for i, j, k in combinations_with_replacement(elements, 3) if i + j + k == 0]

print(tuples)
