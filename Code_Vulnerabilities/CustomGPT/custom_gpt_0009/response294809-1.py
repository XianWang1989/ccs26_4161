
import itertools
import numpy as np  # You should import numpy if you're using np.array

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Initialize an empty list to hold arrays for each dictionary
formula = []

for item in list_of_data:
    # Fetch values for 'a', 'b', and 'c'
    la = item['a']
    lb = item['b']
    lc = item['c']

    # Calculate the formula results and convert to a list
    results = [(a**2) + 2*b*c for a, b, c in zip(la, lb, lc)]
    formula.append(results)

# Update each dictionary in list_of_data with the corresponding formula result
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])

# Display the results
print("formula =", formula)
print("list_of_data =", list_of_data)
