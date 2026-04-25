
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into train and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Create individual classifiers
clf1 = LogisticRegression(random_state=1)
clf2 = SVC(probability=True, random_state=1)  # SVC needs probability=True for voting
clf3 = DecisionTreeClassifier(random_state=1)

# Fit classifiers on respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('logistic', clf1), 
    ('svc', clf2), 
    ('decision_tree', clf3)
], voting='soft')  # Use 'soft' for probability voting

# Fit the Voting Classifier on one of the datasets
voting_clf.fit(X1_train, y1_train)  # You can choose any dataset for fitting

# Evaluate the ensemble model
accuracy = voting_clf.score(X1_test, y1_test)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
