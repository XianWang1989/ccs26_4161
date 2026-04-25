
import itertools

def foo(lst):
    # Generate all combinations of + and - for each element in the list
    possibilities = []
    for signs in itertools.product(*[(num, -num) for num in lst]):
        possibilities.append(list(signs))
    return possibilities

# Example usage:
print(foo([-4]))  # [[4], [-4]]
print(foo([1, 1]))  # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))  # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
