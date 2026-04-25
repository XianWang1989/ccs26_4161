
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array
array_serialized = json.dumps(array.tolist())

# Deserialize back to NumPy array
array_deserialized = np.array(json.loads(array_serialized))

print("Serialized:", array_serialized)
print("Deserialized:", array_deserialized)
