
import numpy as np
import h5py

# Assuming l and r are your left and right labels in binary form
combined_labels = np.zeros((len(l), 1), dtype=np.int_)
combined_labels[l.flatten() == 1] = 0  # Left arrow
combined_labels[r.flatten() == 1] = 1  # Right arrow

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_combined', data=combined_labels.astype(np.int_), **comp_kwargs)  # New combined label
