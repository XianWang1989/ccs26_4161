
with h5py.File(train_filename, 'w') as f:
    # Existing datasets
    f.create_dataset('label_lr', data=np.argmax(np.vstack((l, r)), axis=0).astype(np.int_), **comp_kwargs)
