
# Modify label definition for left/right handling at data gathering 
label_left_right = np.zeros((N, 1))  # Initialize for N samples
for i in range(N):
    if l[i] == 1 and r[i] == 0:
        label_left_right[i] = 0  # Left pressed
    elif l[i] == 0 and r[i] == 1:
        label_left_right[i] = 1  # Right pressed
    else:
        label_left_right[i] = 0  # or 1, depending on your requirements

# Include in HDF5 dataset
f.create_dataset('label_left_right', data=label_left_right.astype(np.int_), **comp_kwargs)
