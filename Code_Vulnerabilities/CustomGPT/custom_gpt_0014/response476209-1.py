
# Combine left/right into a single label
label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[<condition_for_right>] = 1  # Set to 1 for right key pressed

with h5py.File(train_filename, 'w') as f:
    ...
    f.create_dataset('label_lr', data=label_lr, **comp_kwargs)
