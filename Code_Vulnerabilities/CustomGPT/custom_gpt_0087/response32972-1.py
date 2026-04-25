
import itertools

def generate(n):
    # Create product of [0, 1] repeated n times
    return list(itertools.product([0, 1], repeat=n))

# Example usage
combinations = generate(4)
for combo in combinations:
    print(combo)
