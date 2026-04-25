
import itertools

def generate(n):
    # Generate all possible combinations of 0 and 1 of length n
    return list(itertools.product([0, 1], repeat=n))

# Example usage
print(generate(4))
