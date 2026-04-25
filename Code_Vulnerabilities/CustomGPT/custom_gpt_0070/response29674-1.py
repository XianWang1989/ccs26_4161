
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array
serialized_array = json.dumps(array.tolist())

# Print the serialized JSON
print(serialized_array)

# Deserialize back to a NumPy array
deserialized_array = np.array(json.loads(serialized_array))

# Print the deserialized NumPy array
print(deserialized_array)
