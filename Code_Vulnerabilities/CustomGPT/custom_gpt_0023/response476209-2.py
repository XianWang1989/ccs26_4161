
label_lr = np.where(left, 0, np.where(right, 1, 0))  # 0 for left, 1 for right
