
import h5py
import numpy as np

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combine left/right labels into one
    label_lr = np.argmax(np.array([l, r]), axis=0)  # 0 for left, 1 for right
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
