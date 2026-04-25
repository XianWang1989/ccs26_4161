
import itertools

def foo(numbers):
    # Create a list of lists containing positive and negative combinations
    possibilities = []
    for signs in itertools.product([-1, 1], repeat=len(numbers)):
        possibility = [sign * abs(num) for sign, num in zip(signs, numbers)]
        possibilities.append(possibility)
    return possibilities

# Examples
print(foo([-4]))  # [[4], [-4]]
print(foo([1, 1]))  # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
