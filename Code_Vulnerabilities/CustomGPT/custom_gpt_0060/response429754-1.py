
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels from the SVM classifier
true_labels = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # 1 is positive class, 0 is negative class
predicted_labels = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0]  # SVM predicted labels

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate False Acceptance Rate (FAR) and False Rejection Rate (FRR)
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
