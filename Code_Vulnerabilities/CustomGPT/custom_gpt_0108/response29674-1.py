
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Serialize using simplejson
json_data = json.dumps(array.tolist())

# Print the serialized JSON data
print(json_data)
