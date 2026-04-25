
# Assuming `l` and `r` are your original left and right labels
label_lr = np.where(l == 1, 0, np.where(r == 1, 1, 0))  # 0 for left, 1 for right, 0 for none
