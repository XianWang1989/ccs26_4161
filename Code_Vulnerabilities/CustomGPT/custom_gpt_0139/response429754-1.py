
from sklearn.metrics import confusion_matrix

# Example ground truth labels and the predicted labels from the SVM classifier
# 1 represents positive class (authorized) and 0 represents negative class (unauthorized)

y_true = [1, 0, 1, 1, 0, 1, 0, 0]  # Actual labels
y_pred = [1, 0, 1, 0, 0, 1, 0, 1]  # Predicted labels from SVM

# Generate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculating FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
