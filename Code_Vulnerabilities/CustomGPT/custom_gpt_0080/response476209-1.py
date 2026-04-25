
label_lr = np.select([l == 1, r == 1], [0, 1], default=2)  # 0 for left, 1 for right, 2 for none
