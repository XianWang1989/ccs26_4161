
import itertools
import numpy as np  # Import numpy for array handling

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
    for key, value in item.items():  # use .items() in Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []
# Modify this loop to group results in pairs
for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create a temporary list to collect the formula results for each input
    temp_formula = []
    for a, b, c in zip(la, lb, lc):
        temp_formula.append((a**2) + 2 * b * c)

    # Append the temp_formula to the main formula as a list
    formula.append(temp_formula)

# Update list_of_data with the new formula values
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # convert to np.array for consistency
    list_of_data[k].update(result)

# Output the result
print("Formula:", formula)
print("List of Data:", list_of_data)
