
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels from your SVM model
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # True labels (1 = positive, 0 = negative)
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]  # Predicted labels from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero
far = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero

# Print results
print("False Acceptance Rate (FAR):", far)
print("False Rejection Rate (FRR):", frr)
