
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Splitting into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Create different classifiers for each dataset
clf1 = DecisionTreeClassifier(random_state=1)
clf2 = RandomForestClassifier(random_state=2)
clf3 = DecisionTreeClassifier(random_state=3)

# Fit the models
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1),
    ('rf', clf2),
    ('dt2', clf3)
], voting='hard')

# Fit the voting classifier
# Since all datasets have the same samples, we can stack features
X_train_combined = np.hstack((X1_train, X2_train, X3_train))
y_train_combined = y1_train  # or y2_train, or y3_train; they are similar

voting_clf.fit(X_train_combined, y_train_combined)

# Make predictions
X_test_combined = np.hstack((X1_test, X2_test, X3_test))
y_pred = voting_clf.predict(X_test_combined)

# Evaluate the model
accuracy = accuracy_score(y1_test, y_pred)  # Use the appropriate y_test
print(f'Ensemble model accuracy: {accuracy:.2f}')
