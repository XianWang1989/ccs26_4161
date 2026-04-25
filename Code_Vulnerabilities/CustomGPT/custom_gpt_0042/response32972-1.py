
from itertools import product

def generate_combinations(n):
    # Generate combinations of 0s and 1s for length n
    return list(product([0, 1], repeat=n))

# Example usage
n = 4
combinations = generate_combinations(n)
for combo in combinations:
    print(combo)
