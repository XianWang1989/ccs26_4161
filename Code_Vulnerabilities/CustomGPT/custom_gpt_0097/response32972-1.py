
from itertools import product

def generate(n):
    return list(product([0, 1], repeat=n))

print(generate(4))
