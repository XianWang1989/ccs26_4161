
# Assuming you've modified your data gathering to have combined labels
f.create_dataset('label_left_right', data=combined_labels.astype(np.int_), **comp_kwargs)
