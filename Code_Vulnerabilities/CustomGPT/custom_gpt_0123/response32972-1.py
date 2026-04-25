
import itertools

def generate_combinations(n):
    # Create a list of binary choices (0 and 1)
    return list(itertools.product([0, 1], repeat=n))

print(generate_combinations(4))
