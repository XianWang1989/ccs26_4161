
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
arr_list = arr.tolist()

# Serialize using SimpleJSON
serialized_data = json.dumps(arr_list)

# To deserialize
deserialized_data = json.loads(serialized_data)
# Convert back to a NumPy array
arr_deserialized = np.array(deserialized_data)

print("Serialized Data:", serialized_data)
print("Deserialized Array:\n", arr_deserialized)
