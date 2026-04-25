
import itertools

def foo(numbers):
    # Generate all combinations of positive and negative values
    possibilities = [[(-1 if num < 0 else 1) * abs(num) for num in numbers]
                    for signs in itertools.product([-1, 1], repeat=len(numbers))]
    return possibilities

# Examples of how to use the function
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))             # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))         # [[1, -1, 1], [1, -1, -1], [1, 1, 1], [1, 1, -1],
                               #  [-1, -1, 1], [-1, -1, -1], [-1, 1, 1], [-1, 1, -1]]
