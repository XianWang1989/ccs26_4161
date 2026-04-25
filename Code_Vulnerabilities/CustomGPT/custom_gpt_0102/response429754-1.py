
import numpy as np
from sklearn.metrics import confusion_matrix

# True labels (1 for positive, 0 for negative)
true_labels = np.array([1, 1, 0, 1, 0, 0, 1, 0])
# Predicted labels from SVM classifier
predicted_labels = np.array([1, 0, 0, 1, 1, 0, 0, 0])

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

# Output the results
print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
