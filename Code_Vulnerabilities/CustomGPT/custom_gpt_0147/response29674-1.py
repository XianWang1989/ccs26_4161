
import numpy as np
import simplejson as json

# Step 2: Create a NumPy array
numpy_array = np.array([[1, 2, 3], [4, 5, 6]])

# Step 3: Convert to list
array_list = numpy_array.tolist()

# Step 4: Serialize using simplejson
serialized_json = json.dumps(array_list)

# Step 5: Print the serialized JSON string
print(serialized_json)
