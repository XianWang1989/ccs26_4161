
import numpy as np
import simplejson as json

# Create a NumPy array
numpy_array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = numpy_array.tolist()

# Serialize the list using simplejson
serialized_data = json.dumps(array_list)

print("Serialized JSON Data:")
print(serialized_data)
