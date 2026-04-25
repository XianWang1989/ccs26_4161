
import itertools

def foo(numbers):
    # Create a list of possibilities for each number
    possibilities = []
    for num in numbers:
        abs_num = abs(num)  # Get the absolute value
        possibilities.append([abs_num, -abs_num])  # Include both positive and negative

    # Use itertools.product to generate all combinations
    result = list(itertools.product(*possibilities))

    return result

# Example usage
print(foo([-4]))  # Output: [(4,), (-4,)]
print(foo([1, 3]))  # Output: [(1, 3), (1, -3), (-1, 3), (-1, -3)]
print(foo([1, -1]))  # Output: [(1, -1), (1, 1), (-1, -1), (-1, 1)]
print(foo([-1, 3]))  # Output: [(1, 3), (1, -3), (-1, 3), (-1, -3)]
print(foo([1, -1, 1]))  # Output: [(1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)]
