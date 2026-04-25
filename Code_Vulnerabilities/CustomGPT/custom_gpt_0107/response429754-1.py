
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels from SVM
true_labels = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1])  # 1 for positive class, 0 for negative class
predicted_labels = np.array([1, 0, 1, 0, 0, 1, 1, 0, 0])  # SVM predictions

# Calculate the confusion matrix
TN, FP, FN, TP = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate False Acceptance Rate (FAR) and False Rejection Rate (FRR)
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
