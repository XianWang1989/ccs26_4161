
import itertools

def foo(numbers):
    # Create a list of possible signs for each number
    sign_combinations = list(itertools.product([-1, 1], repeat=len(numbers)))

    # Generate the final combinations of numbers with positive and negative signs
    result = []
    for signs in sign_combinations:
        combination = [sign * abs(num) for sign, num in zip(signs, numbers)]
        result.append(combination)

    return result

# Test cases
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))          # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]
