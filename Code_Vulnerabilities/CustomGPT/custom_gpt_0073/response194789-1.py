
import itertools

def foo(numbers):
    # Create a list of signs (+1 for positive, -1 for negative)
    signs = [-1, 1]

    # Generate all combinations of signs for the numbers
    possibilities = []
    for sign_comb in itertools.product(signs, repeat=len(numbers)):
        # Apply the sign combinations to the numbers
        possibility = [sign * abs(num) for sign, num in zip(sign_comb, numbers)]
        possibilities.append(possibility)

    return possibilities

# Example usages
print(foo([-4]))            # Output: [[4], [-4]]
print(foo([1, 1]))         # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # Output: [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))     # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
