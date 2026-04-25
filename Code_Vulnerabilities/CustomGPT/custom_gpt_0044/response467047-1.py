
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
classifier1 = DecisionTreeClassifier()
classifier2 = SVC(probability=True)  # SVC requires probability=True for voting
classifier3 = LogisticRegression()

classifier1.fit(X1_train, y1_train)
classifier2.fit(X2_train, y2_train)
classifier3.fit(X3_train, y3_train)

# Create the voting ensemble classifier
voting_classifier = VotingClassifier(estimators=[
    ('dt', classifier1),
    ('svc', classifier2),
    ('lr', classifier3)
], voting='soft')  # 'soft' voting uses predicted probabilities

# Fit the voting classifier on the same datasets
X_ensemble_train = np.concatenate((X1_train, X2_train, X3_train))
y_ensemble_train = np.concatenate((y1_train, y2_train, y3_train))

voting_classifier.fit(X_ensemble_train, y_ensemble_train)

# Evaluate on the held-out test data from one of the datasets
X_ensemble_test = np.concatenate((X1_test, X2_test, X3_test))
y_ensemble_test = np.concatenate((y1_test, y2_test, y3_test))

accuracy = voting_classifier.score(X_ensemble_test, y_ensemble_test)
print(f'Ensemble model accuracy: {accuracy:.2f}')
