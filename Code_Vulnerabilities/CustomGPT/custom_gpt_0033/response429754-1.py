
from sklearn.metrics import confusion_matrix

# Example: true labels and predicted labels
true_labels = [1, 1, 0, 1, 0, 0, 1, 0]  # 1 = positive, 0 = negative
predicted_labels = [1, 0, 0, 1, 1, 0, 1, 0]

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn)  # False Acceptance Rate
frr = fn / (fn + tp)  # False Rejection Rate

# Print results
print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
