
from sklearn import metrics

# Sample data
y_true = [1, 0, 1, 0, 1]  # True labels (1=positive, 0=negative)
y_pred = [1, 1, 0, 0, 1]  # Predicted labels from SVM

# Confusion matrix
conf_matrix = metrics.confusion_matrix(y_true, y_pred)
TN, FP, FN, TP = conf_matrix.ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (TP + FN) if (TP + FN) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
