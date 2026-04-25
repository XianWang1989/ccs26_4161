
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels (1 for positive, 0 for negative)
y_true = np.array([1, 1, 0, 1, 0, 0, 1, 0])
# Example predicted labels from SVM
y_pred = np.array([1, 0, 0, 1, 1, 0, 0, 0])

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

# Print results
print("False Acceptance Rate (FAR):", FAR)
print("False Rejection Rate (FRR):", FRR)
