
import numpy as np

# Sample actual and predicted labels
# 1 = positive class, 0 = negative class
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0])
y_pred = np.array([1, 0, 0, 1, 1, 0, 0, 1])

# Calculate False Acceptances (FA) and False Rejections (FR)
false_acceptances = np.sum((y_true == 0) & (y_pred == 1))
false_rejections = np.sum((y_true == 1) & (y_pred == 0))

# Calculate total counts for each class
total_negatives = np.sum(y_true == 0)
total_positives = np.sum(y_true == 1)

# Calculate FAR and FRR
FAR = false_acceptances / total_negatives if total_negatives > 0 else 0
FRR = false_rejections / total_positives if total_positives > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
