
import itertools

def generate(n):
    return list(itertools.product([0, 1], repeat=n))

# Example usage:
result = generate(4)
# Convert tuples to lists if you want the output to be in list format
result_as_lists = [list(item) for item in result]
print(result_as_lists)
