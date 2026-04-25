from itertools import product

lst = [-4, -2, 1, 2, 5, 0]
result = [tup for tup in product(lst, repeat=3) if sum(tup) == 0]

print(result)
