
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import numpy as np

# Sample data and labels
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0])  # True labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0])  # Predicted labels from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (tp + fn) if (tp + fn) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
