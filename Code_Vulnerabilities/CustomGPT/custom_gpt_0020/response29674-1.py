
import numpy as np
import simplejson as json

# Create a sample NumPy array
numpy_array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = numpy_array.tolist()

# Serialize the list using SimpleJSON
serialized_data = json.dumps(array_list)

# Display the serialized output
print("Serialized JSON:", serialized_data)

# To deserialize back to a NumPy array
deserialized_data = json.loads(serialized_data)
numpy_array_back = np.array(deserialized_data)

# Display the original NumPy array
print("Deserialized NumPy Array:\n", numpy_array_back)
