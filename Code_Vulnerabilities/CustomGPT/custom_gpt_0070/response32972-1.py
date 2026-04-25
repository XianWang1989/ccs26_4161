
import itertools

def generate_combinations(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage
combinations = generate_combinations(4)
for combination in combinations:
    print(combination)
