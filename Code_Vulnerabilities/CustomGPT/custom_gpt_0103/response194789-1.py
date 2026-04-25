
import itertools

def foo(numbers):
    possibilities = []
    options = []

    for num in numbers:
        if num > 0:
            options.append([num, -num])
        else:
            options.append([-num, num])

    # Create all combinations of the options
    for combination in itertools.product(*options):
        possibilities.append(list(combination))

    return possibilities

# Example usage
print(foo([-4]))         # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]
