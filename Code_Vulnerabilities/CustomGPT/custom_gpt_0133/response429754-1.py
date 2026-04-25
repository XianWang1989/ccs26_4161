
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Use only two classes for binary classification
X = X[y != 2]
y = y[y != 2]

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and fit the SVM model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn)  # False Acceptance Rate
FRR = fn / (fn + tp)  # False Rejection Rate

print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
