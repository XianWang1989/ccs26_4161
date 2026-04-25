
import itertools

def generate(n):
    # Generate all combinations of 0s and 1s of length n
    return list(itertools.product([0, 1], repeat=n))

# Call the function with the desired length
result = generate(4)
print(result)
