
# Combine left and right labels into a single label
label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[left == 1] = 0  # Left pressed
label_lr[right == 1] = 1  # Right pressed
