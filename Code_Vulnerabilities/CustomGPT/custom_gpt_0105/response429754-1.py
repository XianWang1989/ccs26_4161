
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

# Sample data: true labels and predicted labels from SVM
y_true = np.array([1, 1, 0, 1, 0, 0, 1, 0])  # Ground truth (1: Positive, 0: Negative)
y_pred = np.array([1, 0, 0, 1, 0, 1, 0, 0])  # Predicted labels from SVM

# Confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

# Output the results
print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
