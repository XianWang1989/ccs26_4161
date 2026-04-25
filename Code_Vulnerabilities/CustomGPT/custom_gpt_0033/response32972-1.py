
import itertools

def generate(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage
combinations = generate(4)
for combo in combinations:
    print(combo)
