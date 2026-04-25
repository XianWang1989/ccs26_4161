
# Update labels to combine left and right into a single label
combined_labels = np.zeros((N, 1), dtype=np.int_)
combined_labels[np.where(l == 1)] = 0  # Left pressed
combined_labels[np.where(r == 1)] = 1  # Right pressed
