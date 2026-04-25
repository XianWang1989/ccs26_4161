
import h5py
import numpy as np

# Compression options for HDF5
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)

    # Merged label for left/right
    merged_labels = np.where(l.astype(np.int_) == 1, 0, 1)  # 0 for left, 1 for right
    f.create_dataset('label_lr', data=merged_labels, **comp_kwargs)
