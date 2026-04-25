
from itertools import product

def foo(numbers):
    possibilities = []
    for signs in product([-1, 1], repeat=len(numbers)):
        possibilities.append([sign * abs(num) for sign, num in zip(signs, numbers)])
    return possibilities

# Example usage:
print(foo([-4]))
print(foo([1, 1]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
