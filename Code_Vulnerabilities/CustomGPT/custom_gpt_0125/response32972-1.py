
import itertools

def generate_combinations(n):
    return list(itertools.product([0, 1], repeat=n))

combinations = generate_combinations(4)
print(combinations)
