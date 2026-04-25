
from sklearn.metrics import confusion_matrix

# Example true and predicted labels
y_true = [1, 0, 1, 0, 1]  # Actual labels
y_pred = [1, 1, 0, 0, 1]  # Predicted labels

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fara = fp / (fp + tn) if (fp + tn) > 0 else 0
frr = fn / (fn + tp) if (fn + tp) > 0 else 0

# Output results
print(f'False Acceptance Rate (FAR): {fara:.2f}')
print(f'False Rejection Rate (FRR): {frr:.2f}')
