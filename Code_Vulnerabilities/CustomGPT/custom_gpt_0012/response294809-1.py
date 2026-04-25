
import itertools
import numpy as np

list_of_data = [{'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
                {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
                {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

# Separate keys with corresponding values
formula = []

for item in list_of_data:
    la = item['a'].tolist()
    lb = item['b'].tolist()
    lc = item['c'].tolist()

    current_formula = []  # Store values for the current dictionary
    for a, b, c in zip(la, lb, lc):
        current_formula.append((a ** 2) + 2 * b * c)

    formula.append(current_formula)  # Append the current formula list

for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Update with the array for current formula
    list_of_data[k].update(result)

print("Formula =", formula)
print("List of Data =", list_of_data)
