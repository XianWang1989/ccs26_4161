
from itertools import product

def generate_combinations(n):
    return list(product([0, 1], repeat=n))

# Example: Generating combinations for a list of length 4
combinations = generate_combinations(4)
for combo in combinations:
    print(combo)
