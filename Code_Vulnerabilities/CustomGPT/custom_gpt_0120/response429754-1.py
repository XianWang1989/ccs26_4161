
import numpy as np
from sklearn import metrics

# Actual labels (ground truth)
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
# Predicted labels from the SVM classifier
y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 1])

# Calculate confusion matrix
tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn)  # False Acceptance Rate
FRR = fn / (fn + tp)  # False Rejection Rate

print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
