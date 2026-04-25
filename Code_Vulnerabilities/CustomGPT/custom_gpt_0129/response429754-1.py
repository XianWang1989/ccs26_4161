
from sklearn.metrics import confusion_matrix

# Assuming y_true are the true labels and y_pred are the predicted labels
# For example:
y_true = [1, 0, 1, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fap = fp / (fp + tn) if (fp + tn) > 0 else 0  # handle division by zero
frp = fn / (tp + fn) if (tp + fn) > 0 else 0  # handle division by zero

print(f"False Acceptance Rate (FAR): {fap:.2f}")
print(f"False Rejection Rate (FRR): {frp:.2f}")
