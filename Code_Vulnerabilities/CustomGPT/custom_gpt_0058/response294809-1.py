
import itertools
import numpy as np  # Assuming you are using NumPy arrays

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():  # Change to items() for Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []
for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create a list to hold the results for this index
    current_formula = []

    for a, b, c in zip(la, lb, lc):  # Use zip instead of itertools.izip
        current_formula.append((a**2) + 2*b*c)

    # Append the list of results to the formula
    formula.append(current_formula)

for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Use NumPy array for consistency
    list_of_data[k].update(result)

# Outputs
print("formula =", formula)
print("list_of_data =", list_of_data)
