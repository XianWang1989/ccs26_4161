
# Assuming l and r are your existing labels
label_lr = np.where(l == 1, 0, np.where(r == 1, 1, -1))  # -1 if neither is pressed
