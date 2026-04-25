
import numpy as np
import h5py

# Example input data variables
X = ...  # Your image data
S = ...  # Your speed data

# Initialize your labels
N = len(X)  # Assuming this corresponds to the number of samples
label_forward = np.zeros((N, 1), dtype=np.int_)
label_backward = np.zeros((N, 1), dtype=np.int_)
label_left = np.zeros((N, 1), dtype=np.int_)
label_right = np.zeros((N, 1), dtype=np.int_)

# Populate your labels (example logic)
for i in range(N):
    command = get_command_from_data(i)  # An example function to retrieve command from your data
    if command == 'forward':
        label_forward[i] = 1
    elif command == 'backward':
        label_backward[i] = 1
    elif command == 'left':
        label_left[i] = 1
        label_right[i] = 0  # Ensure left/right conflict
    elif command == 'right':
        label_right[i] = 1
        label_left[i] = 0  # Ensure left/right conflict

# Store to HDF5
with h5py.File('train_data.h5', 'w') as f:
    f.create_dataset('data_img', data=X, compression='gzip', compression_opts=1)
    f.create_dataset('data_speed', data=S.astype(np.float_), compression='gzip', compression_opts=1)
    f.create_dataset('label_forward', data=label_forward, compression='gzip', compression_opts=1)
    f.create_dataset('label_backward', data=label_backward, compression='gzip', compression_opts=1)
    f.create_dataset('label_left', data=label_left, compression='gzip', compression_opts=1)
    f.create_dataset('label_right', data=label_right, compression='gzip', compression_opts=1)
