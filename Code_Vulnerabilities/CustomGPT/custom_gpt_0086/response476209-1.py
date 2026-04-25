
import h5py
import numpy as np

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

# Assuming X, S, f, b, l, and r are already defined datasets
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Modify left and right labels for mutually exclusive control
    label_lr = np.zeros((N, 1), dtype=np.int_)
    label_lr[r.flatten() == 1] = 1  # Right
    label_lr[l.flatten() == 1] = 0  # Left

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_left_right', data=label_lr, **comp_kwargs)

with open(train_filename_list_txt, 'w') as f:
    f.write(train_filename + '\n')
