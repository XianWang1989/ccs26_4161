
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array
serialized_data = json.dumps(arr.tolist())

# To deserialize back to a NumPy array
deserialized_arr = np.array(json.loads(serialized_data))

print("Serialized Data:", serialized_data)
print("Deserialized Array:\n", deserialized_arr)
