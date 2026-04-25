
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Convert to list for serialization
arr_list = arr.tolist()

# Serialize the list
serialized = json.dumps(arr_list)

# Output the serialized string
print(serialized)

# To deserialize back to a NumPy array
deserialized = json.loads(serialized)
arr_back = np.array(deserialized)

print(arr_back)
