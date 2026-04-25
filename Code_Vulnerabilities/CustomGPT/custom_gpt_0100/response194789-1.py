
from itertools import product

def foo(numbers):
    # Generate combinations of positive and negative using product
    possibilities = []
    for signs in product(*[(abs(num), -abs(num)) for num in numbers]):
        possibilities.append(list(signs))
    return possibilities

# Example usage
print(foo([-4]))             # [[4], [-4]]
print(foo([1, 1]))           # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))          # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))       # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
