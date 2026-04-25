
# New label representation for left/right
label_lr = np.zeros(N)  # Shape (N,)
label_lr[condition_for_right] = 1  # Set to 1 if right key
