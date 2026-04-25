
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels
y_true = [1, 1, 0, 1, 0, 0, 1, 0]  # Actual labels
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]  # Predicted labels from SVM

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn)  # False Acceptances (FP) / (FP + TN)
FRR = fn / (fn + tp)  # False Rejections (FN) / (FN + TP)

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
