
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample actual and predicted labels
# 1 represents a positive class (match), 0 represents a negative class (non-match)
actual_labels = np.array([1, 0, 1, 1, 0, 0, 1])
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 0])

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(actual_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptances / Total Non-Matches
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejections / Total Matches

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
