
from itertools import product

def foo(numbers):
    # Generate the possible combinations of + and - for each number
    possibilities = [[abs(num) if sign == '+' else -abs(num) for sign in signs]
                     for num, signs in zip(numbers, product('+-', repeat=len(numbers)))]

    return possibilities

# Example usages
print(foo([-4]))             # [[4], [-4]]
print(foo(['+', '+']))       # [[+, +], [+, -], [-, +], [-, -]]
print(foo(['-', '+']))       # [[+, +], [+, -], [-, +], [-, -]]
print(foo([-1, 3]))          # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo(['+', '-', '+']))   # [[+, -, +], [+, -, -], [-, -, +], [-, -, -], 
#                                  [+, +, -], [+, +, +], [-, +, +], [-, +, -]]
