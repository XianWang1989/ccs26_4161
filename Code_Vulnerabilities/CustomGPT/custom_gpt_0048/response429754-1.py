
import numpy as np
from sklearn import metrics

# Sample actual and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0, 0, 1])  # Actual labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 0, 1])  # Predicted labels from SVM

# Calculate confusion matrix
confusion_matrix = metrics.confusion_matrix(y_true, y_pred)
TN, FP, FN, TP = confusion_matrix.ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN)  # False Acceptance Rate
FRR = FN / (FN + TP)  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {FAR:.4f}")
print(f"False Rejection Rate (FRR): {FRR:.4f}")
