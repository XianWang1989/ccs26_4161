
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample actual and predicted labels
actual_labels = np.array([1, 1, 0, 0, 1, 0, 1])  # Ground truth labels
predicted_labels = np.array([1, 0, 0, 0, 0, 1, 1])  # Model predictions

# Calculate the confusion matrix
tn, fp, fn, tp = confusion_matrix(actual_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
