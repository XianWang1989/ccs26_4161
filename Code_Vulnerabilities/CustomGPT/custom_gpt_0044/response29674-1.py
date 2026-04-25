
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array by converting it to a list
serialized = json.dumps(arr.tolist())

print(serialized)  # Outputs the serialized JSON string

# Deserialize back to a NumPy array
deserialized = np.array(json.loads(serialized))

print(deserialized)  # Outputs the original NumPy array
