
import itertools

def generate_combinations(n):
    return [list(combo) for combo in itertools.product([0, 1], repeat=n)]

# Example usage
combinations = generate_combinations(4)
print(combinations)
