
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels
true_labels = np.array([1, 1, 0, 1, 0, 0, 1, 0])  # 1 is positive class, 0 is negative class
predicted_labels = np.array([1, 0, 0, 1, 1, 0, 0, 0])

# Calculate the confusion matrix
TN, FP, FN, TP = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0  # To avoid division by zero
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0  # To avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
