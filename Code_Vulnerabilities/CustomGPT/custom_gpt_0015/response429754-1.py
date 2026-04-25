
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])  # Actual labels
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0])  # Predicted labels

# Calculate confusion matrix
TN, FP, FN, TP = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (TP + FN) if (TP + FN) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR}")
print(f"False Rejection Rate (FRR): {FRR}")
