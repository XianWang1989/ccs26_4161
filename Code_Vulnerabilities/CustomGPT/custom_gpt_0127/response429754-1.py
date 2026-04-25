
import numpy as np

# Example true labels and predicted labels
true_labels = np.array([1, 0, 1, 1, 0, 0, 1])  # 1: positive, 0: negative
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 1])  # SVM predictions

# Calculate FAR and FRR
def calculate_frr_fa(true, predicted):
    # True Positives (TP): predicted positive and actually positive
    tp = np.sum((true == 1) & (predicted == 1))
    # False Negatives (FN): predicted negative but actually positive
    fn = np.sum((true == 1) & (predicted == 0))
    # False Positives (FP): predicted positive but actually negative
    fp = np.sum((true == 0) & (predicted == 1))

    # Calculate FRR and FAR
    frr = fn / (fn + tp) if (fn + tp) > 0 else 0
    far = fp / (fp + (len(true) - np.sum(true))) if (fp + (len(true) - np.sum(true))) > 0 else 0

    return frr, far

frr, far = calculate_frr_fa(true_labels, predicted_labels)
print(f"FRR: {frr:.2f}, FAR: {far:.2f}")
