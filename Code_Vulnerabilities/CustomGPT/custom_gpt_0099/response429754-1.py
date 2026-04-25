
from sklearn.metrics import confusion_matrix

# Assuming you have your true labels and predicted labels
y_true = [1, 1, 0, 0, 1, 0, 1, 0]  # True labels (1 = positive, 0 = negative)
y_pred = [1, 0, 0, 0, 1, 0, 1, 1]  # Predicted labels from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn)  # False Positive Rate
FRR = fn / (fn + tp)  # False Negative Rate

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
