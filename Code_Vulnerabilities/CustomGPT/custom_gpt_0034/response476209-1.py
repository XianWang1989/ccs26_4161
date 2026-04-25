
# Modify the labels
# Now 'label_lr' has three possible values: 
# 0 = left, 1 = right, 2 = none
label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[l == 1, 0] = 0  # left pressed
label_lr[r == 1, 0] = 1   # right pressed
# For both keys or none, ensure to have conditions that prevent simultaneous presses.
