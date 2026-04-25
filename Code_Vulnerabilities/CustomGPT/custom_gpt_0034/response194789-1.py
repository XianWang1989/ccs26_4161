
from itertools import product

def foo(int_list):
    # Generate combinations of positive and negative
    possibilities = []
    signs = [1, -1]  # 1 for positive, -1 for negative

    # Create a product of the signs for each number in the list
    for sign_combination in product(signs, repeat=len(int_list)):
        # Create the new combination based on the current sign combination
        combination = [abs(num) * sign for num, sign in zip(int_list, sign_combination)]
        possibilities.append(combination)

    return possibilities

# Example usages
print(foo([-4]))             # [[4], [-4]]
print(foo([1, 1]))           # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))          # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))       # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1]]
