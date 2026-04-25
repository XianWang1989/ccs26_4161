
# Modify left/right labels to be single binary class
label_lr = np.where(left_labels == 1, 0, 1)  # 0 for left, 1 for right
