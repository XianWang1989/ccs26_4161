
import itertools

def generate_combinations(n):
    # Creates a list of 0s and 1s, repeated n times
    return list(itertools.product([0, 1], repeat=n))

# Example usage
combinations = generate_combinations(4)
for combo in combinations:
    print(combo)
