
import itertools

def generate_combinations(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage
result = generate_combinations(4)
for combo in result:
    print(combo)
