
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combine left and right arrow keys
    f.create_dataset('label_direction', data=np.vstack((l, r)).T.astype(np.int_), **comp_kwargs)

# Create a train filename list
with open(train_filename_list_txt, 'w') as f:
    f.write(train_filename + '\n')
