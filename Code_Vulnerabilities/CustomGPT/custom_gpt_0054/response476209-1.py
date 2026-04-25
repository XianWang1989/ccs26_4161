
import h5py
import numpy as np

# Sample data shapes
N = 1000  # Number of samples
K, H, W = 3, 64, 64  # Channels, Height, Width for the images

X = np.random.rand(N, K, H, W)  # Image data
S = np.random.rand(N, 1)  # Speed data
f = np.random.randint(0, 2, N)  # Forward labels
b = np.random.randint(0, 2, N)  # Backward labels
lr = np.random.randint(0, 3, N)  # LeftRight combined labels

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_lr', data=lr.astype(np.int_), **comp_kwargs)  # Combined label
