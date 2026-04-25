
from itertools import product

def generate(n):
    return list(product([0, 1], repeat=n))

# Example usage
result = generate(4)
for combination in result:
    print(combination)
