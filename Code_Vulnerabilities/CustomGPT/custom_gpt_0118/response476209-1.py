
import numpy as np
import h5py

# Assuming your original left and right labels are binary (0 or 1)
# Create combined labels
combined_labels = np.argmax(np.column_stack([l, r]), axis=1)

# Now save your data using HDF5
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_combined', data=combined_labels.astype(np.int_), **comp_kwargs)

with open(train_filename_list_txt, 'w') as f:
    f.write(train_filename + '\n')
