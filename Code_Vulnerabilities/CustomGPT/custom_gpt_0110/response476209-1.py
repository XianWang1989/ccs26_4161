
import h5py
import numpy as np

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)  # Shape: N x K x H x W
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)  # Shape: N x 1

    f.create_dataset('label_forward', data=forward_labels.astype(np.int_), **comp_kwargs)  # Shape: N x 1
    f.create_dataset('label_backward', data=backward_labels.astype(np.int_), **comp_kwargs)  # Shape: N x 1
    f.create_dataset('label_left_right', data=left_right_labels.astype(np.int_), **comp_kwargs)  # Shape: N x 1

# Save filename list
with open(train_filename_list_txt, 'w') as f:
    f.write(train_filename + '\n')
