
# Combine left and right labels into a single label
# This can be represented as 0 for left and 1 for right
label_lr_combined = np.where(l == 1, 0, r)  # 0 for left, 1 for right
