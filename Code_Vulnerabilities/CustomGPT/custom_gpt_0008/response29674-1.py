
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Serialize using simplejson
serialized_array = json.dumps(array.tolist())

print(serialized_array)  # Output: [1, 2, 3, 4, 5]

# To deserialize back to a NumPy array
deserialized_array = np.array(json.loads(serialized_array))

print(deserialized_array)  # Output: [1 2 3 4 5]
