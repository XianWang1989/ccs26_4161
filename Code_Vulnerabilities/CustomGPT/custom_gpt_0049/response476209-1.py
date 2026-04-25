
# Assuming label_left and label_right are your original labels
label_lr = np.vstack((l, r)).T  # Stack labels left and right
label_lr = np.argmax(label_lr, axis=1)  # Assuming 0 for left and 1 for right
