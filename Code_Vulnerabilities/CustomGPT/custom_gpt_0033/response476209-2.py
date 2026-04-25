
# Create combined labels for left/right control
label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[(l == 1) & (r == 0)] = 0  # Left pressed
label_lr[(r == 1) & (l == 0)] = 1  # Right pressed
label_lr[(l == 0) & (r == 0)] = 2  # None pressed

with h5py.File(train_filename, 'w') as f:
    # Storing images and speed remains the same
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Updated labels to include combined left and right
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)
