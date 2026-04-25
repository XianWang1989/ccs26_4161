
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Generate synthetic datasets for illustration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into training and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train different classifiers on each dataset
clf1 = LogisticRegression()
clf1.fit(X_train1, y_train1)

clf2 = DecisionTreeClassifier()
clf2.fit(X_train2, y_train2)

clf3 = SVC(probability=True)  # Set probability=True for soft voting
clf3.fit(X_train3, y_train3)

# Create an ensemble model using VotingClassifier
ensemble_clf = VotingClassifier(estimators=[
    ('logistic', clf1),
    ('decision_tree', clf2),
    ('svc', clf3)
], voting='soft')

# Train the ensemble classifier on any of the datasets (using X_train1 here)
ensemble_clf.fit(X_train1, y_train1)

# Make predictions on the test data (using X_test1 here)
predictions = ensemble_clf.predict(X_test1)

# Evaluate your model
accuracy = ensemble_clf.score(X_test1, y_test1)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
