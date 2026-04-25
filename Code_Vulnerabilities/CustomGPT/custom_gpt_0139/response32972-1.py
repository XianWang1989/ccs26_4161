
from itertools import product

def generate(n):
    return list(product([0, 1], repeat=n))

# Example usage:
print(generate(4))
