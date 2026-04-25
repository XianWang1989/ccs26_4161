
from sklearn.metrics import confusion_matrix
import numpy as np

# Example predicted and actual labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1])  # Actual labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1])  # Predicted labels

# Generate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
total_negatives = tn + fp
total_positives = tp + fn

far = fp / total_negatives if total_negatives > 0 else 0
frr = fn / total_positives if total_positives > 0 else 0

print(f"False Acceptance Rate (FAR): {far:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
