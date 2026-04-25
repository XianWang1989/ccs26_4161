
# Example for merging left and right labels
# Assume 'left' and 'right' are the original labels
label_lr = np.zeros((num_samples, 1), dtype=np.int_)
label_lr[left == 1] = 0  # Label 0 for left
label_lr[right == 1] = 1  # Label 1 for right
