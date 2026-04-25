
from sklearn.metrics import confusion_matrix

# Assume these are your true labels and the predicted labels from your SVM
y_true = [0, 0, 1, 1, 0, 1]  # Replace with actual true labels
y_pred = [0, 1, 1, 1, 0, 0]  # Replace with actual predictions

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejection Rate

print(f'False Acceptance Rate (FAR): {fpr:.2f}')
print(f'False Rejection Rate (FRR): {frr:.2f}')
