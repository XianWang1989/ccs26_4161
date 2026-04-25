
from sklearn import metrics
import numpy as np

# Sample true labels and predicted labels from SVM
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0, 0, 1])  # 1 = positive, 0 = negative
y_pred = np.array([1, 1, 1, 0, 0, 0, 1, 0, 1, 1])  # Predicted labels

# Calculate confusion matrix
tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
