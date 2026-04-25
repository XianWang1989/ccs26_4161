
from sklearn.metrics import confusion_matrix

# Example predicted labels and true labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # True labels
y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]  # Predicted labels

# Calculate the confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fAR = fp / (fp + tn)  # False Acceptance Rate
fRR = fn / (fn + tp)  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {fAR:.2f}")
print(f"False Rejection Rate (FRR): {fRR:.2f}")
