
import itertools

def generate(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage
result = generate(4)
for combination in result:
    print(combination)
