
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_lr', data=label_lr_combined.astype(np.int_), **comp_kwargs)
