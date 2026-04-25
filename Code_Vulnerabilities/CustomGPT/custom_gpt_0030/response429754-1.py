
import numpy as np

# Example true labels and predicted labels
true_labels = np.array([1, 0, 1, 0, 1])  # 1 = positive, 0 = negative
predicted_labels = np.array([1, 1, 0, 0, 1])  # SVM model predictions

# Calculate Confusion Matrix Components
TP = np.sum((true_labels == 1) & (predicted_labels == 1))  # True Positives
TN = np.sum((true_labels == 0) & (predicted_labels == 0))  # True Negatives
FP = np.sum((true_labels == 0) & (predicted_labels == 1))  # False Positives
FN = np.sum((true_labels == 1) & (predicted_labels == 0))  # False Negatives

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (TP + FN) if (TP + FN) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
