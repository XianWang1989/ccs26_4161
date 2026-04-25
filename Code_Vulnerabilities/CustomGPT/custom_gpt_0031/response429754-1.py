
import numpy as np
from sklearn import metrics

# Example true labels and predicted labels
y_true = np.array([1, 1, 0, 1, 0, 0, 1, 0])  # Actual labels (1: genuine, 0: impostor)
y_pred = np.array([1, 0, 0, 1, 1, 0, 0, 0])  # Predicted labels from SVM

# Calculate False Accepts and False Rejects
false_accepts = np.sum((y_pred == 1) & (y_true == 0))  # 1 predicted as 1 but true is 0
false_rejects = np.sum((y_pred == 0) & (y_true == 1))  # 0 predicted as 0 but true is 1

# Total counts
total_non_matching_attempts = np.sum(y_true == 0)  # Total impostor attempts
total_matching_attempts = np.sum(y_true == 1)      # Total genuine attempts

# Calculate FAR and FRR
FAR = false_accepts / total_non_matching_attempts if total_non_matching_attempts > 0 else 0
FRR = false_rejects / total_matching_attempts if total_matching_attempts > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
