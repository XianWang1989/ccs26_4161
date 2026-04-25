
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generate sample datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2)

# Train individual classifiers
clf1 = RandomForestClassifier()
clf2 = SVC(probability=True)
clf3 = LogisticRegression()

clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble classifier
ensemble_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)
], voting='soft')

# Train the ensemble model on the combined train sets
X_combined = np.vstack((X1_train, X2_train, X3_train))
y_combined = np.hstack((y1_train, y2_train, y3_train))

ensemble_clf.fit(X_combined, y_combined)

# Evaluate on the combined test sets
X_test_combined = np.vstack((X1_test, X2_test, X3_test))
y_test_combined = np.hstack((y1_test, y2_test, y3_test))
accuracy = ensemble_clf.score(X_test_combined, y_test_combined)

print(f"Ensemble model accuracy: {accuracy:.2f}")
