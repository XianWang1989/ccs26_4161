label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[l[:, 0] == 1] = 0  # 0 = left
label_lr[r[:, 0] == 1] = 1  # 1 = right
