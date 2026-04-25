
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np

# Sample dataset (features and labels)
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.randint(2, size=100)  # Binary labels: 0 or 1

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM Classifier
classifier = SVC(probability=True)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Calculate confusion matrix
tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (tp + fn) if (tp + fn) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
