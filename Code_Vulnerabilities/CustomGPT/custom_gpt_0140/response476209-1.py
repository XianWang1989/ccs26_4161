
# Assuming label_left and label_right are already created
label_lr = np.where(label_left == 1, 0, 1)  # 0 for left, 1 for right
f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)
