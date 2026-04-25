
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combine left and right labels
    label_lr = np.zeros((N, 1), dtype=np.int_)
    # Populate label_lr based on your logic
    f.create_dataset('label_lr', data=label_lr, **comp_kwargs)
