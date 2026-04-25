
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert it to a list
array_list = array.tolist()

# Serialize the list to JSON
json_data = json.dumps(array_list)

print(json_data)
