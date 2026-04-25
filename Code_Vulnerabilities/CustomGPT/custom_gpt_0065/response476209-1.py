
# Assuming l and r are your left and right labels, both are binary (0 or 1).
combined_labels = np.zeros((N, 1), dtype=np.int_)

for i in range(N):
    if l[i] == 1:
        combined_labels[i] = 0  # 0 for left
    elif r[i] == 1:
        combined_labels[i] = 1  # 1 for right
    else:
        combined_labels[i] = -1  # -1 for none
