
# When creating your labels, redefine how you assign left/right
import numpy as np

# Assuming l and r are your existing labels
label_direction = np.zeros((N, 1), dtype=np.int_)
for i in range(N):
    if l[i] == 1 and r[i] == 0:
        label_direction[i] = 0  # left
    elif r[i] == 1 and l[i] == 0:
        label_direction[i] = 1  # right
    else:
        label_direction[i] = 2  # neutral (both are 0)

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_direction', data=label_direction, **comp_kwargs)
