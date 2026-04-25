
from sklearn.metrics import confusion_matrix

# Assume y_true are your true labels and y_pred are your predicted labels
y_true = [0, 1, 0, 1, 1, 0, 1, 0]  # Example true labels
y_pred = [0, 1, 1, 0, 1, 0, 0, 0]  # Example predicted labels

# Compute confusion matrix
TN, FP, FN, TP = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
