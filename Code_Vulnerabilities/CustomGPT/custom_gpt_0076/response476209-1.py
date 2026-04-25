
import h5py
import numpy as np

# Assuming l and r are the original left and right label arrays
label_lr = np.where(l == 1, 0, np.where(r == 1, 1, 0))

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)  # Merged labels
