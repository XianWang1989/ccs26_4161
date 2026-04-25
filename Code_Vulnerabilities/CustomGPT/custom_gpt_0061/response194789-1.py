
def foo(lst):
    from itertools import product

    # Generate all combinations of signs for the input list
    signs = product([-1, 1], repeat=len(lst))

    # Create the result list with the combinations
    result = [[sign * abs(num) for sign, num in zip(signs_combination, lst)] 
              for signs_combination in signs]

    return result

# Example usages
print(foo([-4]))
print(foo([1, 1]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
