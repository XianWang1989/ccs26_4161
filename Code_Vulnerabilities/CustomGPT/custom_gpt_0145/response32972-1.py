
import itertools

def generate(n):
    return list(itertools.product(*([[0, 1]] * n)))

# Example usage
combinations = generate(4)
print(combinations)
