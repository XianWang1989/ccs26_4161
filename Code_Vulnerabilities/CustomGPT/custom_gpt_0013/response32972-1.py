
import itertools

def generate_combinations(n):
    return list(itertools.product([0, 1], repeat=n))

# Generate combinations for a list of length 4
combinations = generate_combinations(4)
for comb in combinations:
    print(comb)
