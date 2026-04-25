
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Creating three different datasets with similar labels
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Splitting datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Training individual classifiers
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()
clf3 = SVC(probability=True)

clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Getting predictions from each classifier
pred1 = clf1.predict(X1_test)
pred2 = clf2.predict(X2_test)
pred3 = clf3.predict(X3_test)

# Creating a voting classifier
voting_classifier = VotingClassifier(estimators=[
    ('lr', clf1),
    ('dt', clf2),
    ('svc', clf3)],
    voting='soft'  # Use 'hard' for majority voting, 'soft' for based on predicted probabilities
)

# For the voting classifier, you generally train it on the original datasets or a combination of them.
# Here, we'll suppose you're combining predictions from individual classifiers.
# Note: It's common to train the VotingClassifier directly on a combined dataset instead.
# Using the predictions could be useful for further clarifying approaches.

# A simple way to get the final predictions
# (Example only, normally we would fit on combined data instead)
voting_classifier.fit(X1_train, y1_train)  # Usually, you'd combine your datasets and train
final_predictions = voting_classifier.predict(X1_test)

# Evaluating the performance of the ensemble model
accuracy = accuracy_score(y1_test, final_predictions)
print(f'Ensemble model accuracy: {accuracy:.2f}')
