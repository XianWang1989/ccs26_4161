
# Modify the label data creation
combined_lr = np.where(l == 1, 0, r)  # 0 for left press, 1 for right, 2 for no press
f.create_dataset('label_lr', data=combined_lr.astype(np.int_), **comp_kwargs)
