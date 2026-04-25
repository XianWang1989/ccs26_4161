
import itertools

def generate(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage
print(generate(4))
