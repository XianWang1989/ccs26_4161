
from itertools import product

result = [tup for tup in product([-4, -2, 1, 2, 5, 0], repeat=3) if sum(tup) == 0]
print(result)
