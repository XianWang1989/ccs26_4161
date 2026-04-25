
# Assuming label_left and label_right are numpy arrays of shape (N,)
# Create a combined label (0: left, 1: right)
combined_label = np.argmax(np.column_stack((label_left, label_right)), axis=1)  # 0 for left, 1 for right
