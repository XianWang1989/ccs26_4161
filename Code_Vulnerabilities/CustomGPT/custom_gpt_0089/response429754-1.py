
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels from SVM
y_true = np.array([0, 1, 1, 0, 1, 0, 1, 0])  # True labels
y_pred = np.array([0, 1, 0, 0, 1, 0, 1, 1])  # Predicted labels

# Generate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Prevent division by zero
FRR = fn / (tp + fn) if (tp + fn) > 0 else 0  # Prevent division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
