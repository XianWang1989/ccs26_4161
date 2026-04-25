
# Sample true labels and predicted labels
true_labels = [1, 1, 0, 1, 0, 0, 1, 0]  # 1: Positive, 0: Negative
predicted_labels = [1, 0, 0, 1, 1, 0, 0, 0]

# Convert to numpy arrays for easier calculations
import numpy as np

true_labels = np.array(true_labels)
predicted_labels = np.array(predicted_labels)

# Calculate FAR
false_acceptances = np.sum((true_labels == 0) & (predicted_labels == 1))
total_negatives = np.sum(true_labels == 0)
FAR = false_acceptances / total_negatives if total_negatives > 0 else 0

# Calculate FRR
false_rejections = np.sum((true_labels == 1) & (predicted_labels == 0))
total_positives = np.sum(true_labels == 1)
FRR = false_rejections / total_positives if total_positives > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
