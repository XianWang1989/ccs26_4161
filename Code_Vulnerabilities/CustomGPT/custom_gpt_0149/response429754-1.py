
from sklearn.metrics import confusion_matrix

# Assuming y_true is the true labels and y_pred is the predicted labels from your SVM
y_true = [1, 0, 1, 1, 0, 1, 0, 0]  # Example true labels
y_pred = [1, 0, 1, 0, 0, 1, 1, 0]  # Example predictions from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
far = fp / (fp + tn) if (fp + tn) > 0 else 0  # Prevent division by zero
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # Prevent division by zero

print(f'False Acceptance Rate (FAR): {far:.2f}')
print(f'False Rejection Rate (FRR): {frr:.2f}')
