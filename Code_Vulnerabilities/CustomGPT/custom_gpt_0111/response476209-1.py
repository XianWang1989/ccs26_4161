
# Fusion of left and right labels
label_left_right = np.where(l == 1, 0, np.where(r == 1, 1, -1))  # 0 for left, 1 for right, -1 for none
