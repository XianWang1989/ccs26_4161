
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train classifiers on each dataset
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)
clf3 = RandomForestClassifier(random_state=3)

clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Get predictions on the test set (make sure to use the same test set)
pred1 = clf1.predict(X1_test)
pred2 = clf2.predict(X2_test)
pred3 = clf3.predict(X3_test)

# Combine predictions using VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf1', clf1),
    ('gb', clf2),
    ('rf2', clf3)
], voting='hard')

# Fit on one of the training sets (you can choose any)
voting_clf.fit(X1_train, y1_train)

# Get final predictions
final_pred = voting_clf.predict(X1_test)

# Calculate accuracy
accuracy = accuracy_score(y1_test, final_pred)
print(f'Accuracy of the ensemble model: {accuracy:.2f}')
