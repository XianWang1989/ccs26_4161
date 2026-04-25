
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels
true_labels = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 0])  # Ground truth
predicted_labels = np.array([1, 0, 1, 0, 0, 0, 1, 1, 0, 0])  # Model predictions

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Only if there are negative samples
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Only if there are positive samples

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
