
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels from SVM
y_true = np.array([0, 0, 1, 1, 0, 1])  # 0 = Negative, 1 = Positive
y_pred = np.array([0, 1, 1, 0, 0, 1])  # Predicted labels

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
far = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Accepts / Total Negatives
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejects / Total Positives

print(f"False Acceptance Rate (FAR): {far:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
