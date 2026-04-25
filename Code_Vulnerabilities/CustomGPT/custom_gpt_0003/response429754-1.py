
from sklearn import metrics

# Sample true labels and predicted labels from SVM
true_labels = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]  # Ground truth (actual labels)
predicted_labels = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]  # Your SVM predictions

# Calculate the confusion matrix
tn, fp, fn, tp = metrics.confusion_matrix(true_labels, predicted_labels).ravel()

# False Acceptance Rate (FAR)
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0

# False Rejection Rate (FRR)
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
