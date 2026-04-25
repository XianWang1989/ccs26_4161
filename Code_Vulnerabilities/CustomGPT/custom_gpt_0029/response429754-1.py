
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

# Example ground truth labels (1 = positive, 0 = negative)
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0])
# Example predicted labels from SVM
y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0])

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
