
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Serialize the NumPy array
serialized_arr = json.dumps(arr.tolist())

# Print the serialized output
print(serialized_arr)

# Deserialize back to a NumPy array
deserialized_arr = np.array(json.loads(serialized_arr))

# Print the deserialized output
print(deserialized_arr)
