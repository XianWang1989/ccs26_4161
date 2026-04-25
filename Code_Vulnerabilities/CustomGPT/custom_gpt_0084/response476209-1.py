
# Assuming left and right keys are encoded as numpy arrays
# where 0 represents left pressed, 1 represents right, and 2 represents neither
labels_lr = np.where(l == 1, 0, np.where(r == 1, 1, 2))  # Replace with your logic
