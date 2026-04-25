
# Assuming `l` and `r` are already defined as arrays of 0s and 1s,
# where `l` = 1 when the left key is pressed else 0,
# and `r` = 1 when the right key is pressed else 0.

# Create a combined left/right label
label_lr_combined = np.maximum(l, r)  # Effectively 1 if right is pressed, otherwise it will be 0 if left is pressed
f.create_dataset('label_lr', data=label_lr_combined.astype(np.int_), **comp_kwargs)
