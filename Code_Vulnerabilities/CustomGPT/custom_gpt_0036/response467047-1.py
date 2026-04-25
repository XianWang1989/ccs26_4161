
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generating synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Create classifiers for each dataset
clf1 = DecisionTreeClassifier(random_state=42)
clf2 = RandomForestClassifier(random_state=42)
clf3 = LogisticRegression(random_state=42)

# Fit each classifier on its own dataset
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble of these classifiers
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1), 
    ('rf', clf2), 
    ('lr', clf3)], 
    voting='hard'
)

# Combine predictions
# Note: The test set used here is from the first dataset, adjust as needed
voting_clf.fit(X1_train, y1_train)
predictions = voting_clf.predict(X1_test)

# Evaluate the ensemble classifier
accuracy = accuracy_score(y1_test, predictions)
print(f'Accuracy of the ensemble model: {accuracy:.2f}')
