
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_f', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_b', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_lr', data=labels_lr.astype(np.int_), **comp_kwargs)  # Merged labels
