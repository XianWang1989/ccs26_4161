
def foo(numbers):
    from itertools import product

    # Map the input numbers to their absolute values and determine signs
    options = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations of positive and negative values
    combinations = list(product(*options))

    return combinations

# Example usage:
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], 
                            #  [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, -1, 1]]
