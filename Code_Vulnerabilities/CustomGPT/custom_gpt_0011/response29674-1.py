
import numpy as np
import simplejson as json

# Create a NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])

# Serialize the NumPy array to a JSON string
json_string = json.dumps(numpy_array.tolist())

# Print the serialized JSON string
print(json_string)
