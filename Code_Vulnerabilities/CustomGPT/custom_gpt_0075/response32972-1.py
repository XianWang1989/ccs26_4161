
from itertools import product

def generate(n):
    return list(product([0, 1], repeat=n))

# Test with n=4
print(generate(4))
