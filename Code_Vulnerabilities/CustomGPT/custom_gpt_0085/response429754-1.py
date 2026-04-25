
import numpy as np
from sklearn.metrics import confusion_matrix

# Example ground truth labels and predicted labels from SVM
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0])  # True labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0])  # Predicted labels by SVM

# Calculate confusion matrix
TN, FP, FN, TP = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0  # False Acceptance Rate
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
