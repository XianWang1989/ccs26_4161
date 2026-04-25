
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = np.array([1, 0, 1, 0, 1, 0, 1])  # Actual labels (1 - positive, 0 - negative)
predicted_labels = np.array([1, 0, 0, 0, 1, 1, 1])  # Predicted labels from SVM

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
