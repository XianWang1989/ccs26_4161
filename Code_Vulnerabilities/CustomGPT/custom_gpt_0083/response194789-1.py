
def foo(numbers):
    from itertools import product

    # Convert input numbers to their positive/negative versions
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Generate the Cartesian product of the positive and negative versions
    result = list(product(*possibilities))

    return result

# Example usage:
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))             # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
                                #  [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
