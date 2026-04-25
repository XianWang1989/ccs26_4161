
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Generate sample data for three different datasets
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split each dataset into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train classifiers on each dataset
model1 = RandomForestClassifier(random_state=1)
model2 = GradientBoostingClassifier(random_state=2)
model3 = RandomForestClassifier(random_state=3)

model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Combine classifiers in a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf1', model1),
    ('gb', model2),
    ('rf2', model3)],
    voting='hard')  # or 'soft' for probability-based voting

# Fit the ensemble model on the first dataset's training data
voting_clf.fit(X1_train, y1_train)

# Predict and evaluate
y_pred = voting_clf.predict(X1_test)
accuracy = accuracy_score(y1_test, y_pred)

print(f"Ensemble model accuracy: {accuracy:.2f}")
