
fused_labels = np.where(r == 1, 1, np.where(l == 1, 0, 1))  # 0 for left, 1 for right or both off
f.create_dataset('label_lr', data=fused_labels.astype(np.int_), **comp_kwargs)
