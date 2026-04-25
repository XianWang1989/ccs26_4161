
import itertools

def generate(n):
    return [list(item) for item in itertools.product([0, 1], repeat=n)]

print(generate(4))
