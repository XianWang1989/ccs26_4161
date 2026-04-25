
# Assuming `left` and `right` are numpy arrays containing the original labels
combined_labels = np.where(left == 1, 0, 1)
