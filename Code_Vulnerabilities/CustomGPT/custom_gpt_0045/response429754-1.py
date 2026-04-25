
import numpy as np
from sklearn.metrics import confusion_matrix

# Example actual and predicted labels (0 for negative, 1 for positive)
y_true = np.array([0, 1, 1, 0, 1, 0, 0, 1, 0, 1])  # Actual labels
y_pred = np.array([0, 0, 1, 1, 1, 0, 0, 0, 0, 1])  # Predicted labels by SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
