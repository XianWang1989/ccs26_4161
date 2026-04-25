
import itertools

def foo(numbers):
    possibilities = []

    # Generate the cartesian product of positive and negative versions
    for signs in itertools.product(*[(-1, 1) for _ in numbers]):
        possibilities.append([sign * abs(num) for sign, num in zip(signs, numbers)])

    return possibilities

# Example usage:
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))             # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1]]
