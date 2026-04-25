
# Assuming `label_left` and `label_right` are binary (0 or 1):
label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[l == 1, 0] = 0  # Left key pressed
label_lr[r == 1, 0] = 1  # Right key pressed
