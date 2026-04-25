
import itertools
import numpy as np  # Make sure to import numpy

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

formula = []  # This will hold lists of formulas for each dictionary

# Loop through the data to separate keys with corresponding values
for item in list_of_data:
    list_of_a = item['a'].tolist()
    list_of_b = item['b'].tolist()
    list_of_c = item['c'].tolist()

    # Calculate the formula for the current item
    current_formula = []
    for a, b, c in zip(list_of_a, list_of_b, list_of_c):
        current_formula.append((a**2) + 2*b*c)

    formula.append(current_formula)  # Append the list of formulas for this dictionary

# Update each dictionary with the new formula list
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Store as a numpy array
    list_of_data[k].update(result)

print("formula =", formula)
print("list_of_data =", list_of_data)
