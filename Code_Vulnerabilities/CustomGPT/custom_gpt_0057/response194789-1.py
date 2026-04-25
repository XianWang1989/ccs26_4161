
import itertools

def foo(lst):
    possibilities = []
    signs = [1, -1]

    for combination in itertools.product(signs, repeat=len(lst)):
        new_list = [abs(num) * sign for num, sign in zip(lst, combination)]
        possibilities.append(new_list)

    return possibilities

# Example usage
print(foo([-4]))
print(foo([1, 1]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
