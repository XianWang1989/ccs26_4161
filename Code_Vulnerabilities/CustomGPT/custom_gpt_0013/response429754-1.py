
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels
# 1 = positive class (accept), 0 = negative class (reject)
true_labels = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 0, 1, 1, 0])

# Calculate confusion matrix
TN, FP, FN, TP = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
