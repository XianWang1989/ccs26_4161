
import numpy as np
import h5py

# Example data arrays - replace these with your actual training data
X = np.random.rand(1000, 3, 64, 64)  # N x C x H x W
S = np.random.rand(1000, 1)
f = np.random.randint(2, size=(1000, 1))  # forward
b = np.random.randint(2, size=(1000, 1))  # backward
l = np.random.randint(2, size=(1000, 1))  # left
r = np.random.randint(2, size=(1000, 1))  # right

# Fusion labels for left and right
leftright = np.where(l == 1, 0, 1)  # 0 for left, 1 for right

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File('train_data.h5', 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_leftright', data=leftright.astype(np.int_), **comp_kwargs)  # Merged label

with open('train_filename_list.txt', 'w') as f:
    f.write('train_data.h5\n')
