
combined_lr = np.zeros((N, 1), dtype=np.int_)
combined_lr[l == 1] = 0  # Left pressed
combined_lr[r == 1] = 1  # Right pressed
combined_lr[(l == 0) & (r == 0)] = 2  # None pressed

with h5py.File(train_filename, 'w') as f:
    # Other datasets...
    f.create_dataset('label_lr', data=combined_lr, **comp_kwargs)
