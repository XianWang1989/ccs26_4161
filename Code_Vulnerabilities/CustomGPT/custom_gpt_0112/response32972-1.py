
from itertools import product

def generate_combinations(n):
    return list(product([0, 1], repeat=n))

print(generate_combinations(4))
