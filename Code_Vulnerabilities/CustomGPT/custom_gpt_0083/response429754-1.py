
import numpy as np
from sklearn import metrics

# Sample true labels and predicted labels
true_labels = np.array([1, 0, 1, 1, 0, 0, 1])  # 1 = positive class, 0 = negative class
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 1])

# Calculate False Acceptance Rate (FAR) and False Rejection Rate (FRR)
def calculate_frr_far(true, predicted):
    # True Positives (TP): Correctly predicted positive
    TP = np.sum((true == 1) & (predicted == 1))
    # True Negatives (TN): Correctly predicted negative
    TN = np.sum((true == 0) & (predicted == 0))
    # False Positives (FP): Incorrectly predicted positive
    FP = np.sum((true == 0) & (predicted == 1))
    # False Negatives (FN): Incorrectly predicted negative
    FN = np.sum((true == 1) & (predicted == 0))

    # Calculate FAR and FRR
    FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
    FRR = FN / (TP + FN) if (TP + FN) > 0 else 0

    return FAR, FRR

fpr, frr = calculate_frr_far(true_labels, predicted_labels)

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
