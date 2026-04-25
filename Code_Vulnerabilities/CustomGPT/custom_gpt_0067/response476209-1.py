
# Create a single label for left and right keys
label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[condition_for_right_keys] = 1  # Change to 1 where right key is pressed
