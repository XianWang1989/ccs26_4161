
from sklearn import metrics
import numpy as np

# Example predictions and ground truth labels
y_true = np.array([1, 0, 1, 1, 0, 1])  # Ground truth labels
y_pred = np.array([1, 0, 0, 1, 0, 0])  # Predictions from SVM

# Function to calculate FAR and FRR
def calculate_frr_fra(y_true, y_pred):
    # Calculate True Positives, False Positives, True Negatives, False Negatives
    tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

    far = fp / (fp + tn)  # False Acceptance Rate
    frr = fn / (fn + tp)  # False Rejection Rate

    return far, frr

# Calculate FAR and FRR
far, frr = calculate_frr_fra(y_true, y_pred)

print(f"False Acceptance Rate (FAR): {far:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
