
import numpy as np
import simplejson as json

# Create a NumPy array
original_array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array to JSON
# Convert the NumPy array to a list
serialized_array = json.dumps(original_array.tolist())

print("Serialized JSON string:")
print(serialized_array)

# Deserialize the JSON string back to a NumPy array
# Load the JSON string to a Python list
deserialized_list = json.loads(serialized_array)
# Convert the list back to a NumPy array
deserialized_array = np.array(deserialized_list)

print("\nDeserialized NumPy array:")
print(deserialized_array)
