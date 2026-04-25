
import itertools
from numpy import array

list_of_data = [
    {'a': array([1, 2]), 'b': array([3, 4]), 'c': array([5, 6])}, 
    {'a': array([7, 8]), 'b': array([9, 10]), 'c': array([1, 2])},
    {'a': array([-1, 4]), 'b': array([1, 10]), 'c': array([4, 5])}
]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []       

for item in list_of_data:
    for key, value in item.items():  # changed from iteritems() to items() for Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist()) 
        elif key == 'c':
            list_of_c.append(value.tolist())

# Initialize an empty list for storing formulas
formula = []

# Compute the formulas for each set of values
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    current_formula = []
    for a, b, c in zip(la, lb, lc):
        current_formula.append((a**2) + 2*b*c)
    formula.append(current_formula)

# Update the list_of_data with the new formula entries
for k in range(len(list_of_data)):
    result = {'formula': array(formula[k])}  # use array for consistency
    list_of_data[k].update(result)

# Output the results
print("formula =", formula)
print("list_of_data =", list_of_data)
