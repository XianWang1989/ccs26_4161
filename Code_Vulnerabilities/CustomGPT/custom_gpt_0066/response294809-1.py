
import itertools
import numpy as np

list_of_data = [
    {'a': np.array([1, 2]),  'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
    {'a': np.array([7, 8]),  'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []       

for item in list_of_data:
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist()) 
        elif key == 'c':
            list_of_c.append(value.tolist())

# Create formula arrays
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    formulas_for_current = []  # Store formulas for the current index
    for a, b, c in zip(la, lb, lc):
        formulas_for_current.append((a ** 2) + 2 * b * c)

    formula.append(formulas_for_current)  # Append the list of formulas to formula

# Update list_of_data with formula arrays
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Store as numpy array
    list_of_data[k].update(result)

# Output the results
print("Formula:", formula)  # Expected: [[31, 52], [67, 104], [9, 116]]
print("List of Data:", list_of_data)
