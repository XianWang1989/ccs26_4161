
with h5py.File(train_filename, 'w') as f:
    # Your other datasets...
    f.create_dataset('label_direction', data=label_direction, **comp_kwargs)
