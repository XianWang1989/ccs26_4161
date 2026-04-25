
import numpy as np
import itertools

list_of_data = [{'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
                 {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
                 {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

# Prepare the lists to gather results
formula = []

# Iterate over each dictionary in the list
for item in list_of_data:
    la = item['a']
    lb = item['b']
    lc = item['c']

    # Calculate the formulas
    temp_formula = [(a**2) + 2*b*c for a, b, c in zip(la, lb, lc)]
    formula.append(temp_formula)

# Update the dictionaries in list_of_data with the new formula
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])

# Print the results
print("formula =", formula)
print("list_of_data =", list_of_data)
