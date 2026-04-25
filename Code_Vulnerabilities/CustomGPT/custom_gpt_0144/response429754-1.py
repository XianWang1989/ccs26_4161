from sklearn.metrics import confusion_matrix

# True labels and predicted labels
y_true = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]  # 1 = genuine, 0 = impostor
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]  # Output from SVM

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn)  # False Acceptance Rate
FRR = fn / (fn + tp)  # False Rejection Rate

print(f"FAR: {FAR:.2f}")
print(f"FRR: {FRR:.2f}")
