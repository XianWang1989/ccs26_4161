
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0, 0, 1])  # Actual labels (1 for positive, 0 for negative)
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 0, 0])  # Predicted labels from SVM

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # For computing FAR, total negatives = tn + fp
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # For computing FRR, total positives = fn + tp

# Output the results
print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
