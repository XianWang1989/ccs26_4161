
import itertools
import numpy as np  # Make sure to import numpy for array functionality

# Sample data
list_of_data = [{'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
                 {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
                 {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []       

for item in list_of_data:
    for key, value in item.items():  # Use .items() instead of .iteritems()
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist()) 
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):  # Use zip instead of itertools.izip
    temp_formula = []  # Store intermediate formulas for each entry
    for a, b, c in zip(la, lb, lc):
        temp_formula.append((a ** 2) + 2 * b * c)
    formula.append(temp_formula)  # Append the complete formula list for this entry

# Update list_of_data with the new formula structure
for index in range(len(list_of_data)):
    list_of_data[index]['formula'] = np.array(formula[index])

# Output results
print("formula =", formula)  # Expected: [[31, 52], [67, 104], [9, 116]]
print("list_of_data =", list_of_data)
