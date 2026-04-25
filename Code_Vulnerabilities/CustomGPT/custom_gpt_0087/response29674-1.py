
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Serialize the array using SimpleJSON
serialized_arr = json.dumps(arr.tolist())

print("Serialized NumPy array:", serialized_arr)

# To deserialize back to NumPy array
deserialized_arr = np.array(json.loads(serialized_arr))

print("Deserialized NumPy array:", deserialized_arr)
