
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array to JSON
json_data = json.dumps(array.tolist())

# Print the JSON string
print(json_data)

# To deserialize back to a NumPy array
decoded_array = np.array(json.loads(json_data))

# Print the reconstructed NumPy array
print(decoded_array)
