
import itertools

def generate(n):
    return list(itertools.product([0, 1], repeat=n))

print(generate(4))
