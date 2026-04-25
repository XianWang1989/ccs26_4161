
import numpy as np
import simplejson as sj

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list using SimpleJSON
serialized_data = sj.dumps(array_list)

# Print the serialized data
print(serialized_data)

# To deserialize it back to a NumPy array
deserialized_data = sj.loads(serialized_data)
array_restored = np.array(deserialized_data)

# Print the restored NumPy array
print(array_restored)
