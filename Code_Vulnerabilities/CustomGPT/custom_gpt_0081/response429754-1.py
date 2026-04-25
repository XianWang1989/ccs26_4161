
from sklearn import svm
from sklearn.metrics import confusion_matrix
import numpy as np

# Sample data: true labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1])  # Actual labels (1: positive, 0: negative)
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1])  # Predicted labels from SVM

# Compute the confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero

print("False Acceptance Rate (FAR):", FAR)
print("False Rejection Rate (FRR):", FRR)
