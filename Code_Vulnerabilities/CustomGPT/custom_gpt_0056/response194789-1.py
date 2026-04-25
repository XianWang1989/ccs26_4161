
def foo(numbers):
    from itertools import product

    # Convert each number to its absolute value and create a sign list
    abs_numbers = [abs(num) for num in numbers]
    signs = [(1, -1) if num != 0 else (0,) for num in numbers]

    # Create all combinations of signs
    combinations = list(product(*signs))

    # Generate the resulting list with all positive and negative possibilities
    results = [[abs_num * sign for abs_num, sign in zip(abs_numbers, combo)] for combo in combinations]

    return results

# Example usages
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
                           #  [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
