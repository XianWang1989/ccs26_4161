
# Assuming you have binary values for left and right:
combined_label = np.where(label_left == 1, 0, np.where(label_right == 1, 1, 2))

# Save to HDF5
f.create_dataset('label_direction', data=combined_label.astype(np.int_), **comp_kwargs)
