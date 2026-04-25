
# Adjust the left and right labels into a single label
label_direction = np.maximum(l, r)  # Assuming l and r are arrays with 0s and 1s for left and right presses
label_direction = label_direction.astype(np.int_)  # Convert to integer
