
# Create combined labels: 0 for left, 1 for right
left_right_labels = np.where(left_pressed, 0, np.where(right_pressed, 1, 0))
