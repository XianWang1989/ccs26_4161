
# Assuming label_left and label_right are already defined
label_lr_combined = np.zeros_like(label_left)

# Combine left and right labels
label_lr_combined[label_left == 1] = 0  # Left key pressed
label_lr_combined[label_right == 1] = 1  # Right key pressed

# Now use label_lr_combined instead of label_left and label_right
