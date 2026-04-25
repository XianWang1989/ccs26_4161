
# Assuming `lr` is an array where 0 is none, 1 is left, and 2 is right
f.create_dataset('label_left_right', data=lr.astype(np.int_), **comp_kwargs)
