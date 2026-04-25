
from sklearn.metrics import confusion_matrix

# Sample true and predicted labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # Actual labels
y_pred = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]  # Predicted labels from SVM

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
total_negatives = tn + fp  # Negative instances
total_positives = tp + fn   # Positive instances

fpr = fp / total_negatives if total_negatives > 0 else 0  # False Acceptance Rate
frr = fn / total_positives if total_positives > 0 else 0  # False Rejection Rate

print(f'False Acceptance Rate (FAR): {fpr:.2f}')
print(f'False Rejection Rate (FRR): {frr:.2f}')
