
from itertools import product

def generate_combinations(n):
    # Use itertools.product to create the Cartesian product, with repeat to control length
    return list(product([0, 1], repeat=n))

# Generate combinations for a list of length 4
combinations = generate_combinations(4)
for combination in combinations:
    print(combination)
