
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels from your SVM classifier
true_labels = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # Actual labels (1 = positive, 0 = negative)
predicted_labels = [1, 0, 0, 1, 0, 1, 0, 0, 1, 1]  # Predicted labels

# Generate confusion matrix
TN, FP, FN, TP = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FRR and FAR
def calculate_frr_fpr(TP, FN, TN, FP):
    FAR = FP / (FP + TN) if (FP + TN) != 0 else 0  # Handling division by zero
    FRR = FN / (FN + TP) if (FN + TP) != 0 else 0  # Handling division by zero
    return FAR, FRR

fpr, frr = calculate_frr_fpr(TP, FN, TN, FP)

print("False Acceptance Rate (FAR): {:.2f}".format(fpr))
print("False Rejection Rate (FRR): {:.2f}".format(frr))
