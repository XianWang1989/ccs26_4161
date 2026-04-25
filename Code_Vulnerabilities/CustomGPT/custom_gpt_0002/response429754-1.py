
import numpy as np

# Assuming you have true labels and predicted labels
# 1 for positive class, 0 for negative class
true_labels = np.array([1, 0, 1, 1, 0, 0, 1, 0])
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 1, 0])

# Calculate False Acceptance Rate (FAR) and False Rejection Rate (FRR)
def calculate_far_frr(true_labels, predicted_labels):
    false_acceptances = np.sum((true_labels == 0) & (predicted_labels == 1))
    false_rejections = np.sum((true_labels == 1) & (predicted_labels == 0))

    # Total negatives and positives
    total_negatives = np.sum(true_labels == 0)
    total_positives = np.sum(true_labels == 1)

    far = false_acceptances / total_negatives if total_negatives > 0 else 0
    frr = false_rejections / total_positives if total_positives > 0 else 0

    return far, frr

far, frr = calculate_far_frr(true_labels, predicted_labels)
print("False Acceptance Rate (FAR):", far)
print("False Rejection Rate (FRR):", frr)
