
import numpy as np
import simplejson as json

# Create a sample NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list using simplejson
serialized_array = json.dumps(array_list)

print(serialized_array)
