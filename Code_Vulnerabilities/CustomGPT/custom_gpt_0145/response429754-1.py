
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels
true_labels = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]  # 1: Positive, 0: Negative
predicted_labels = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]  # Predicted by SVM

# Get confusion matrix
TN, FP, FN, TP = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR (False Acceptance Rate)
FAR = FP / (FP + TN)

# Calculate FRR (False Rejection Rate)
FRR = FN / (TP + FN)

# Print results
print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
