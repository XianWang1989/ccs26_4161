
import numpy as np
from sklearn import metrics

# Assume y_true are the actual labels and y_pred are the predicted labels from your SVM model
y_true = np.array([1, 1, 0, 1, 0, 0, 1, 0])  # Example true labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 0, 0])  # Example predicted labels

# Calculate confusion matrix
tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
