
def foo(numbers):
    from itertools import product

    # Create options for each number: positive and negative
    options = []
    for num in numbers:
        options.append([abs(num), -abs(num)])  # Use abs to handle values irrespective of sign

    # Generate all combinations of the sign variations
    combinations = list(product(*options))

    return combinations

# Example usage
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))             # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
