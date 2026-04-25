
import numpy as np  # Make sure to import numpy for array operations
import itertools

# Input list of dictionaries
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
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Initialize formula as a list of lists
formula = []

for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    formula_entry = []  # Create a new list for the current formula entry

    # Use zip to iterate over a, b, c together
    for a, b, c in zip(la, lb, lc):
        # Update formula_entry with the computed value
        formula_entry.append((a**2) + 2*b*c)

    # Append the formula_entry to the main formula list
    formula.append(formula_entry)

# Update list_of_data with the new 'formula' entries as arrays
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}
    list_of_data[k].update(result)

# Output the result
print("formula =", formula)  # Should output [[31, 52], [67, 104], [9, 116]]
print("list_of_data =", list_of_data)
