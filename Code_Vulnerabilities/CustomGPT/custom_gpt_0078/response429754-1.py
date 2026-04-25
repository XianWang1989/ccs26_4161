
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = [1, 0, 1, 1, 0, 1, 0, 0]  # 1 = match, 0 = non-match
predicted_labels = [1, 0, 1, 0, 0, 1, 1, 0]

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
far = fp / (fp + tn)  # False Acceptance Rate
frr = fn / (fn + tp)  # False Rejection Rate

print(f"FAR (False Acceptance Rate): {far:.2f}")
print(f"FRR (False Rejection Rate): {frr:.2f}")
