
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_horizontal', data=label_horizontal.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_vertical', data=label_vertical.astype(np.int_), **comp_kwargs)  # forward/backward
