
import itertools
import numpy as np

# Assuming arrays are numpy arrays
list_of_data = [{'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
                 {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
                 {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []       

for item in list_of_data:
    list_of_a.append(item['a'])
    list_of_b.append(item['b'])
    list_of_c.append(item['c'])

formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    # Create a list for the current 'formula' entry
    current_formula = []
    for a, b, c in zip(la, lb, lc):
        current_formula.append((a**2) + 2*b*c)
    formula.append(np.array(current_formula))  # Store each formula as a numpy array for consistency

# Update the original list_of_data with the formula
for k in range(len(list_of_data)):
    list_of_data[k].update({'formula': formula[k]})

# Output the result to verify
print(f"formula = {formula}")
print(f"list_of_data = {list_of_data}")
