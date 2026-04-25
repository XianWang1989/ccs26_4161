
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to a list
array_list = array.tolist()

# Serialize using simplejson
json_str = json.dumps(array_list)

print(json_str)
