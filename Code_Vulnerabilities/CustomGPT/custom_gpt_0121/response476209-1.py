
# Modify label_left and label_right to a single label with two classes
label_lr = np.where(l == 1, 0, 1)  # 0 for left, 1 for right
