
from sklearn import metrics
import numpy as np

# Example true labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1, 0])

# Calculate confusion matrix
tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
frr = fn / (tp + fn) if (tp + fn) > 0 else 0

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
