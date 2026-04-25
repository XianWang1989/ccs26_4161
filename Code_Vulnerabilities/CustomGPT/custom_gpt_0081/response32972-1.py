
import itertools

def generate_combinations(n):
    # Generate all combinations of 0s and 1s of length n
    return list(itertools.product([0, 1], repeat=n))

# Example usage
n = 4
combinations = generate_combinations(n)
for combo in combinations:
    print(combo)
