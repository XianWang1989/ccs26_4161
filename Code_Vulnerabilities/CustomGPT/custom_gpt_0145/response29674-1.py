
import numpy as np
import simplejson as json

# Create a NumPy array
np_array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_as_list = np_array.tolist()

# Serialize the list to JSON
json_string = json.dumps(array_as_list)

print(json_string)
