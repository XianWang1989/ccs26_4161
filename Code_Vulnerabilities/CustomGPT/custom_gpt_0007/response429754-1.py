
from sklearn.metrics import confusion_matrix

# Sample predicted labels and ground truth labels
y_true = [1, 0, 1, 1, 0, 1, 0]  # True labels
y_pred = [1, 0, 0, 1, 0, 0, 1]  # Predicted labels by your SVM classifier

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
far = fp / (fp + tn) if (fp + tn) > 0 else 0
frr = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {far:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
