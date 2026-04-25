
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to a list
array_list = array.tolist()

# Serialize using SimpleJSON
serialized = json.dumps(array_list)

# Deserialize back to NumPy array (optional)
deserialized_array = np.array(json.loads(serialized))

print("Serialized JSON:", serialized)
print("Deserialized NumPy array:", deserialized_array)
