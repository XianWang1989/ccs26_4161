
import numpy as np
import itertools

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

formula = []

for item in list_of_data:
    a = item['a']
    b = item['b']
    c = item['c']

    # Calculate the formula for each corresponding element
    result = (a ** 2) + 2 * b * c
    formula.append(result.tolist())  # Append result as a list

for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])  # Update with the array

print("formula =", formula)
print("list_of_data =", list_of_data)
