
from itertools import product

def foo(numbers):
    # Generate a list of '+' and '-' for each number in the input
    signs = []
    for num in numbers:
        if num < 0:
            signs.append([-1, 1])  # Representing '-' and '+' as -1 and 1
        else:
            signs.append([1, -1])

    # Create combinations of signs with the corresponding absolute values
    combinations = []
    for sign_combination in product(*signs):
        combinations.append([abs(num) * sign for num, sign in zip(numbers, sign_combination)])

    return combinations

# Test cases
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [1, 1, -1], [-1, -1, -1], [-1, 1, -1], [-1, -1, 1], [1, 1, 1]]
