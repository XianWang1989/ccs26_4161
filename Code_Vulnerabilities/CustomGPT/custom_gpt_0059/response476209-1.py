
import numpy as np
import h5py

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)

    # Combine left and right labels into a single label
    labels_lr = np.where(l.astype(np.int_) == 1, 0, 1)  # 0 for left, 1 for right
    f.create_dataset('label_lr', data=labels_lr, **comp_kwargs)

# Writing the filename list
with open(train_filename_list_txt, 'w') as f:
    f.write(train_filename + '\n')
