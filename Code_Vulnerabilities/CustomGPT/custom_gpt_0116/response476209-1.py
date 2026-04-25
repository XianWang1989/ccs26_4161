
# Assuming labels have been gathered as follows
# left (0) or right (1)
label_lr = np.where(l == 1, 0, np.where(r == 1, 1, 2))  # 2 for none pressed
