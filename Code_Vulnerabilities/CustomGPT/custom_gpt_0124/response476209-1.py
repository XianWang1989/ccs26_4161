
import numpy as np
import h5py

# Example modifications
# Assuming 'labels' are gathered from your input
# Here, tie_label will be 0 for left and 1 for right
tie_label = np.where(r == 1, 1, 0)  # 0 for left pressed, 1 for right pressed

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_left_right', data=tie_label.astype(np.int_), **comp_kwargs)
