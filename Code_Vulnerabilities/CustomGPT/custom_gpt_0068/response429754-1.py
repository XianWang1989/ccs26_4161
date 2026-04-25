
# Sample true labels and predicted labels
true_labels = [1, 1, 1, 0, 0, 1, 0, 0]  # 1 for positive class, 0 for negative class
predicted_labels = [1, 0, 1, 0, 1, 1, 0, 0]

# Initialize counters
false_acceptances = 0
true_rejections = 0
false_rejections = 0
true_acceptances = 0

for true, pred in zip(true_labels, predicted_labels):
    if true == 1:  # actual positive
        if pred == 0:
            false_rejections += 1  # predicted negative when it was positive
        else:
            true_acceptances += 1  # correctly predicted as positive
    else:  # actual negative
        if pred == 1:
            false_acceptances += 1  # predicted positive when it was negative
        else:
            true_rejections += 1  # correctly predicted as negative

# Calculate FAR and FRR
far = false_acceptances / (false_acceptances + true_rejections) if (false_acceptances + true_rejections) > 0 else 0
frr = false_rejections / (false_rejections + true_acceptances) if (false_rejections + true_acceptances) > 0 else 0

print(f"False Acceptance Rate (FAR): {far:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
