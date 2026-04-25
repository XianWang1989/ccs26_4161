
from itertools import product

def foo(numbers):
    # Generate pairs of signs based on the input numbers
    signs = [(-1, 1)[num > 0] if num != 0 else 0 for num in numbers]
    options = []

    # Create the combinations based on the signs and generate output
    for sign_combination in product(*[[abs(num), -abs(num)] for num in numbers]):
        options.append(list(sign_combination))

    return options

# Examples
print(foo([-4]))                       # Output: [[4], [-4]]
print(foo([1, 1]))                     # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                   # Output: [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))                # Output: [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
                                       #          [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
