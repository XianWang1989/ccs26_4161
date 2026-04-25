
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Train classifiers on each dataset
clf1 = RandomForestClassifier(random_state=1).fit(X1_train, y1_train)
clf2 = LogisticRegression(random_state=2).fit(X2_train, y2_train)
clf3 = SVC(probability=True, random_state=3).fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), ('lr', clf2), ('svm', clf3)],
    voting='soft')  # soft voting uses predicted probabilities

# Fit the ensemble model with predictions from each dataset
combined_X_train = np.column_stack((clf1.predict_proba(X1_test)[:, 1],
                                     clf2.predict_proba(X2_test)[:, 1],
                                     clf3.predict_proba(X3_test)[:, 1]))

combined_X_test = np.column_stack((clf1.predict_proba(X1_test)[:, 1],
                                     clf2.predict_proba(X2_test)[:, 1],
                                     clf3.predict_proba(X3_test)[:, 1]))

# Train the VotingClassifier
voting_clf.fit(combined_X_train, y1_test)  # Using y1_test as labels

# Make predictions
y_pred = voting_clf.predict(combined_X_test)

# Evaluate the ensemble model
accuracy = accuracy_score(y1_test, y_pred)
print(f"Ensemble Model Accuracy: {accuracy:.2f}")
