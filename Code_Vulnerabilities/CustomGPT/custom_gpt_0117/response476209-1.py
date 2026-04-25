
import numpy as np
import h5py

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

# Assuming X, S, f, b, l, and r are already defined arrays
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combine left and right labels into one
    combined_lr = np.where(l == 1, 0, np.where(r == 1, 1, -1))  # -1 for no direction
    f.create_dataset('label_dir', data=combined_lr.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
