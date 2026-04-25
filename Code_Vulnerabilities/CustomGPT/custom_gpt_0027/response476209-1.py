
# Assuming you have left and right labels as binary arrays
combined_labels_lr = np.where(r == 1, 1, np.where(l == 1, 0, -1))  # -1 for no action
