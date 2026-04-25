
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=42)

# Train classifiers on each dataset
clf1 = RandomForestClassifier(random_state=1)
clf1.fit(X1_train, y1_train)

clf2 = LogisticRegression(random_state=2)
clf2.fit(X2_train, y2_train)

clf3 = SVC(probability=True, random_state=3)
clf3.fit(X3_train, y3_train)

# Create an ensemble of the classifiers
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('lr', clf2), 
    ('svc', clf3)], 
    voting='soft')  # Using soft voting for probability predictions

# Fit the ensemble on one of the datasets' training data (or concatenate)
# Here we use the training data from the first dataset
voting_clf.fit(X1_train, y1_train)

# Make predictions
y_pred = voting_clf.predict(X1_test)

# Evaluate the ensemble
accuracy = accuracy_score(y1_test, y_pred)
print(f'Ensemble model accuracy: {accuracy:.2f}')
