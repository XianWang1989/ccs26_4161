
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Simulate three datasets with the same number of samples
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split data into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers
clf1 = SVC(probability=True)  # Classifier for dataset 1
clf2 = DecisionTreeClassifier()  # Classifier for dataset 2
clf3 = LogisticRegression()  # Classifier for dataset 3

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('svc', clf1),
    ('dt', clf2),
    ('lr', clf3)],
    voting='soft'  # Use 'soft' voting for probability averaging
)

# Fit the ensemble model on one of the datasets (ideally, you should have a combined dataset)
ensemble_model.fit(X1_train, y1_train)

# Make predictions
predictions = ensemble_model.predict(X1_test)

# Evaluate
accuracy = np.mean(predictions == y1_test)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
