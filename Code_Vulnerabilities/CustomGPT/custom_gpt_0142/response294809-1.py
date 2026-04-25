
import itertools
import numpy as np  # Make sure to import numpy to use arrays

list_of_data = [
    {'a': np.array([1,2]), 'b': np.array([3,4]), 'c': np.array([5,6])}, 
    {'a': np.array([7,8]), 'b': np.array([9,10]), 'c': np.array([1,2])},
    {'a': np.array([-1,4]), 'b': np.array([1,10]), 'c': np.array([4,5])}
]

# Seperate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():  # Use .items() instead of .iteritems() for Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist()) 
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []  # This will store the list of formulas for each entry

for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Calculate the formula results for respective a, b, c values
    current_formula = []  # Store the current formula results
    for a, b, c in zip(la, lb, lc):  # Use zip instead of itertools.izip for Python 3
        current_formula.append((a**2) + 2*b*c)  # Compute the formula for each
    formula.append(current_formula)  # Append to the formula list

# Now update list_of_data with the new formula values
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Ensure you convert the list to an array
    list_of_data[k].update(result)  # Update the dictionary with the formula

# Print the results
print("formula =", formula)  # Expected: [[31, 52], [67, 104], [9, 116]]
print("list_of_data =", list_of_data)
