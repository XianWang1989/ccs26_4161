
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Train test split
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Initialize classifiers
clf1 = DecisionTreeClassifier()
clf2 = SVC(probability=True)  # SVC needs probability=True for Voting
clf3 = LogisticRegression()

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create voting classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1),
    ('svc', clf2),
    ('lr', clf3)
], voting='soft')  # Using soft voting

# You can use one of the datasets for the final prediction
voting_clf.fit(X1_train, y1_train)  # Fit on one dataset
predictions = voting_clf.predict(X1_test)

# Print predictions
print(predictions)
