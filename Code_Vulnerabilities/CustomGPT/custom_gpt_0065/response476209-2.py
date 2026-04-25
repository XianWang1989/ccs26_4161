
with h5py.File(train_filename, 'w') as f:
    ...
    f.create_dataset('label_lr', data=combined_labels, **comp_kwargs)
