
from itertools import product

def generate_combinations(n):
    return list(product([0, 1], repeat=n))

# Example usage:
combinations = generate_combinations(4)
for combo in combinations:
    print(combo)
