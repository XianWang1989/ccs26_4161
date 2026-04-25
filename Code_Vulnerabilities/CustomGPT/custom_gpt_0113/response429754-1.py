
from sklearn.metrics import confusion_matrix
import numpy as np

# Example true labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0])  # Actual labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 1])  # Predicted labels

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
if (fp + tn) > 0:
    far = fp / (fp + tn)
else:
    far = 0

if (tp + fn) > 0:
    frr = fn / (tp + fn)
else:
    frr = 0

print(f"False Acceptance Rate (FAR): {far:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
