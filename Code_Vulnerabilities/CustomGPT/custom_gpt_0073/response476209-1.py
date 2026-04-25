
import h5py
import numpy as np

# Let's say "l" and "r" are your left and right labels.
label_lr = np.where(l == 1, 0, 1)  # 0 for left, 1 for right or vice versa.

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, compression='gzip')
    f.create_dataset('data_speed', data=S.astype(np.float_), compression='gzip')
    f.create_dataset('label_forward', data=f.astype(np.int_), compression='gzip')
    f.create_dataset('label_backward', data=b.astype(np.int_), compression='gzip')
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), compression='gzip')  # Combined label
