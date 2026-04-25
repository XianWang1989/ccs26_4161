
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array
array_serialized = json.dumps(array.tolist())

# Print the serialized JSON string
print(array_serialized)

# Deserialize back to NumPy array
array_deserialized = np.array(json.loads(array_serialized))

# Print the deserialized array
print(array_deserialized)
