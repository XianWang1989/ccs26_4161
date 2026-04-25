
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Step 1: Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Step 2: Train your classifiers
clf1 = LogisticRegression()
clf2 = RandomForestClassifier()
clf3 = SVC(probability=True)

# Split datasets for training
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Fit classifiers
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Step 3: Create an ensemble model using VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('lr', clf1), 
    ('rf', clf2), 
    ('svc', clf3)
], voting='soft')

# Fit the ensemble model on one of your datasets (you can choose any)
voting_clf.fit(X_train1, y_train1)

# Step 4: Evaluate the ensemble model
predictions = voting_clf.predict(X_test1)
accuracy = accuracy_score(y_test1, predictions)

print(f'Ensemble model accuracy: {accuracy:.2f}')
