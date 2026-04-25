
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array by converting it to a list
serialized_array = json.dumps(array.tolist())

# Print the serialized output
print(serialized_array)

# Deserialize back to a NumPy array
deserialized_array = np.array(json.loads(serialized_array))
print(deserialized_array)
