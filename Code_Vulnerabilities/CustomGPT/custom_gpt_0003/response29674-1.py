
import numpy as np
import simplejson as json

# Create a sample NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
array_list = array.tolist()

# Serialize the list using SimpleJSON
serialized_data = json.dumps(array_list)

print("Serialized NumPy Array:", serialized_data)

# To deserialize back into a NumPy array
deserialized_data = json.loads(serialized_data)
array_from_json = np.array(deserialized_data)

print("Deserialized NumPy Array:\n", array_from_json)
