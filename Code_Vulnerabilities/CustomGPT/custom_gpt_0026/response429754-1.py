
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])  # 1: Positive, 0: Negative
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0])

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn)  # False Acceptance Rate
FRR = fn / (fn + tp)  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
