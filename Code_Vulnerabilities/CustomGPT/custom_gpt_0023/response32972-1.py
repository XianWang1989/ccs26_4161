
from itertools import product

def generate(n):
    return [list(combo) for combo in product([0, 1], repeat=n)]

print(generate(4))
