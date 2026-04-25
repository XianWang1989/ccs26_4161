
label_lr = np.where(l == 1, 0, np.where(r == 1, 1, 2))  # 0 for left, 1 for right, 2 for none
