
import itertools
import numpy as np

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Prepare for the formula calculations
formula = []

for item in list_of_data:
    a = item['a']
    b = item['b']
    c = item['c']

    # Create a new list to store the formulas for the current dictionary
    current_formula = []

    # Calculate the formula for each element in arrays
    for a_val, b_val, c_val in zip(a, b, c):
        current_formula.append((a_val ** 2) + 2 * b_val * c_val)

    formula.append(current_formula)

# Now update the list_of_data with the new formula
for i in range(len(list_of_data)):
    list_of_data[i]['formula'] = np.array(formula[i])

# Output the result
print("Formula:", formula)  # Expected: [[31, 52], [67, 104], [9, 116]]
print("List of data:", list_of_data)
