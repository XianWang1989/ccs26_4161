
from sklearn import metrics

# Assume y_true are the true labels and y_pred are the predicted labels from the SVM
y_true = [1, 0, 1, 0, 1, 0, 1, 0]  # Example true labels (1: positive, 0: negative)
y_pred = [1, 1, 1, 0, 0, 0, 1, 1]  # Example predictions from SVM

# Convert to numpy arrays
y_true = np.array(y_true)
y_pred = np.array(y_pred)

# Calculate True Positives, False Positives, True Negatives, False Negatives
TP = np.sum((y_true == 1) & (y_pred == 1))  # True Positive
FP = np.sum((y_true == 0) & (y_pred == 1))  # False Positive
TN = np.sum((y_true == 0) & (y_pred == 0))  # True Negative
FN = np.sum((y_true == 1) & (y_pred == 0))  # False Negative

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0  # Avoid division by zero
FRR = FN / (TP + FN) if (TP + FN) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
