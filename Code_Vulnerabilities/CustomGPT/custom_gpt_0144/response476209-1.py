import h5py
import numpy as np

# Example dummy data
N = 1000
X = np.random.rand(N, 3, 64, 64)  # image data
S = np.random.rand(N, 1)          # speed
f = np.random.randint(0, 2, (N, 1))  # forward
b = np.random.randint(0, 2, (N, 1))  # backward
l = np.random.randint(0, 2, (N, 1))  # left
r = np.random.randint(0, 2, (N, 1))  # right

with h5py.File('train_data.h5', 'w') as f_out:
    f_out.create_dataset('data_img', data=X, compression='gzip', compression_opts=1)
    f_out.create_dataset('data_speed', data=S.astype(np.float_), compression='gzip', compression_opts=1)
    f_out.create_dataset('label_forward', data=f.astype(np.int_), compression='gzip', compression_opts=1)
    f_out.create_dataset('label_backward', data=b.astype(np.int_), compression='gzip', compression_opts=1)
    f_out.create_dataset('label_left', data=l.astype(np.int_), compression='gzip', compression_opts=1)
    f_out.create_dataset('label_right', data=r.astype(np.int_), compression='gzip', compression_opts=1)
