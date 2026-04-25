
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets (for demonstration)
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define classifiers for each dataset
clf1 = RandomForestClassifier()
clf2 = SVC(probability=True)
clf3 = LogisticRegression()

# Train each classifier on its respective dataset
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)],
    voting='soft')  # Use 'soft' to consider predicted probabilities

# Train the VotingClassifier on combined data (if applicable)
# Here, we can use the same labels as y1, y2, y3 if labels are similar
X_combined = np.vstack((X1_test, X2_test, X3_test))
y_combined = np.concatenate((y1_test, y2_test, y3_test))

voting_clf.fit(X_combined, y_combined)

# Make predictions using the ensemble model
predictions = voting_clf.predict(X_combined)

# Output predictions
print(predictions)
