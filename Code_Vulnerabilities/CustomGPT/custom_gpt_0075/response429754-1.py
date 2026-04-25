
import numpy as np

def calculate_frr_far(y_true, y_pred):
    # Convert inputs to numpy arrays for easier calculations
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Calculate number of positives and negatives
    true_positive = np.sum((y_true == 1) & (y_pred == 1))
    false_positive = np.sum((y_true == 0) & (y_pred == 1))
    false_negative = np.sum((y_true == 1) & (y_pred == 0))
    true_negative = np.sum((y_true == 0) & (y_pred == 0))

    # Calculate FAR and FRR
    FAR = false_positive / (false_positive + true_negative) if (false_positive + true_negative) > 0 else 0
    FRR = false_negative / (false_negative + true_positive) if (false_negative + true_positive) > 0 else 0

    return FAR, FRR

# Example usage
true_labels = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
predicted_labels = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1]

frr, far = calculate_frr_far(true_labels, predicted_labels)
print(f"False Rejection Rate (FRR): {frr:.2f}")
print(f"False Acceptance Rate (FAR): {far:.2f}")
