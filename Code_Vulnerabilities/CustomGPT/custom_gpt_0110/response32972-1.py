
import itertools

def generate_combinations(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage:
print(generate_combinations(4))
