import numpy as np
import itertools

list_of_data = [{'a': np.array([1, 2]),  'b': np.array([3, 4]),  'c': np.array([5, 6])}, 
                {'a': np.array([7, 8]),  'b': np.array([9, 10]), 'c': np.array([1, 2])},
                {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

# Iterate over each dictionary and compute formula for that entry
for item in list_of_data:
    a_vals = item['a']
    b_vals = item['b']
    c_vals = item['c']
    
    formula = [(a**2 + 2*b*c) for a, b, c in zip(a_vals, b_vals, c_vals)]
    
    # Add formula as a numpy array
    item['formula'] = np.array(formula)

# Check result
for entry in list_of_data:
    print(entry)
