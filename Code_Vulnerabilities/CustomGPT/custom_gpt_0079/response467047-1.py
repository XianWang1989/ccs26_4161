
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Simulating three different datasets with the same number of samples
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Splitting datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train classifiers on each dataset
model1 = RandomForestClassifier(random_state=1).fit(X1_train, y1_train)
model2 = LogisticRegression(random_state=1).fit(X2_train, y2_train)
model3 = SVC(probability=True, random_state=1).fit(X3_train, y3_train)

# Creating a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', model1),
    ('lr', model2),
    ('svc', model3)
], voting='soft')  # 'soft' uses predicted probabilities

# Fit the ensemble on one of the datasets (e.g., X1)
voting_clf.fit(X1_train, y1_train)

# Predictions
ensemble_predictions = voting_clf.predict(X1_test)
print("Ensemble predictions:", ensemble_predictions)
