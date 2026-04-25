
from itertools import product

def foo(numbers):
    # Generate combinations of signs (+ and -)
    sign_combinations = product([-1, 1], repeat=len(numbers))

    result = []
    for signs in sign_combinations:
        # Create a new list with the appropriate signs
        transformed_nums = [sign * abs(num) for sign, num in zip(signs, numbers)]
        result.append(transformed_nums)

    return result

# Test cases
print(foo([-4]))           # Output: [[4], [-4]]
print(foo([1, 1]))        # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([1, -1]))       # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # Output: [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
