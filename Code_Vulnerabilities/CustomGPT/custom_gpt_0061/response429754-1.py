
from sklearn.metrics import confusion_matrix

# Example: True labels and predicted labels from your SVM classifier
y_true = [1, 0, 1, 1, 0, 1, 0, 0]  # True labels
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]  # Predicted labels

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
