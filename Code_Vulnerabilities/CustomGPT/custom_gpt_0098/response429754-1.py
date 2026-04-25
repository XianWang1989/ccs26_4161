
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels
true_labels = [1, 0, 1, 1, 0, 0, 1, 0]  # 1 = Positive, 0 = Negative
predicted_labels = [1, 0, 1, 0, 0, 1, 1, 0]

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
