import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list and serialize with simplejson
json_str = json.dumps(arr.tolist())

# Output the JSON string
print(json_str)
