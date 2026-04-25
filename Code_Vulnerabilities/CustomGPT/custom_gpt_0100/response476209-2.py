
# Create combined label for direction
label_direction = np.where(l == 1, 0, np.where(r == 1, 1, 2))
f.create_dataset('label_direction', data=label_direction.astype(np.int_), **comp_kwargs)
