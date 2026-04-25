
# Assuming `l` is the original label_left array and `r` is label_right array
combined_labels = np.where(r == 1, 1, 0)  # 0 if left is pressed, 1 if right is pressed

with h5py.File(train_filename, 'w') as f:
    ...
    f.create_dataset('label_side', data=combined_labels.astype(np.int_), **comp_kwargs)
