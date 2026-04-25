
from itertools import product

def generate(n):
    return list(product([0, 1], repeat=n))

# Example usage:
combinations = generate(4)
for combo in combinations:
    print(combo)
