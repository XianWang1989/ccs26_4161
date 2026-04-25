
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Dummy example, replace with your actual data
X1, y1 = load_iris(return_X_y=True)  # Dataset 1
X2, y2 = load_iris(return_X_y=True)  # Dataset 2
X3, y3 = load_iris(return_X_y=True)  # Dataset 3

# Split each dataset into train and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Train your classifiers
model1 = DecisionTreeClassifier().fit(X1_train, y1_train)
model2 = SVC(probability=True).fit(X2_train, y2_train)  # SVC needs probability=True for voting
model3 = LogisticRegression().fit(X3_train, y3_train)

# Combine models in VotingClassifier
voting_classifier = VotingClassifier(estimators=[
    ('dt', model1),
    ('svc', model2),
    ('lr', model3)
], voting='soft')  # Use soft voting to consider predicted probabilities

# Train the ensemble model
voting_classifier.fit(X1_train, y1_train)  # You can train on one of the datasets

# Make predictions
predictions = voting_classifier.predict(X1_test)

# Evaluate your model
accuracy = voting_classifier.score(X1_test, y1_test)
print(f'Ensemble model accuracy: {accuracy:.2f}')
