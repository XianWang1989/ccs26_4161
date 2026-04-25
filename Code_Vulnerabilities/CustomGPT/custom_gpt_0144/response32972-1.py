import itertools

def generate_binary_combinations(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage
print(generate_binary_combinations(4))
