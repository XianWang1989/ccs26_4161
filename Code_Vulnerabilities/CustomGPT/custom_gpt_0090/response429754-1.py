
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0])  # True labels (1 for positive and 0 for negative)
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0])  # Predicted labels from SVM

# Generate confusion matrix
TN, FP, FN, TP = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
