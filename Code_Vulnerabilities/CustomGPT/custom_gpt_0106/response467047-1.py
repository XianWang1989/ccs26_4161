
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Simulate three datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers on three datasets
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)
clf3 = LogisticRegression(random_state=3)

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('gb', clf2),
    ('lr', clf3)
], voting='hard')  # or use `voting='soft'` for probability-based voting

# Fit the Voting Classifier on one dataset (you could use any)
voting_clf.fit(X1_train, y1_train)

# Make predictions using the Voting Classifier
y_pred = voting_clf.predict(X1_test)

# Evaluate accuracy
accuracy = accuracy_score(y1_test, y_pred)
print(f'Ensemble model accuracy: {accuracy:.2f}')
