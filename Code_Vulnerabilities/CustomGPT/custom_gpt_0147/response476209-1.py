
import h5py
import numpy as np

# Example to create HDF5 dataset
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    # Assuming X and S are predefined
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combined left/right label
    labels_lr = np.where(l == 1, 0, 1)  # Assigning left as 0 and right as 1
    f.create_dataset('label_lr', data=labels_lr.astype(np.int_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)

with open(train_filename_list_txt, 'w') as f:
    f.write(train_filename + '\n')
