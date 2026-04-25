
from sklearn import metrics
import numpy as np

# Sample true labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0])  # Actual labels (1: positive, 0: negative)
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0])  # Predicted labels from SVM

# Confusion Matrix
tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
frr = fn / (fn + tp)  # False Rejection Rate
far = fp / (fp + tn)  # False Acceptance Rate

print(f"False Rejection Rate (FRR): {frr:.2f}")
print(f"False Acceptance Rate (FAR): {far:.2f}")
