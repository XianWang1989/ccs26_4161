
label_lr = np.concatenate((left.reshape(-1, 1), right.reshape(-1, 1)), axis=1).argmax(axis=1)
