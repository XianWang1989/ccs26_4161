
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define classifiers for each dataset
clf1 = RandomForestClassifier(random_state=1)
clf2 = LogisticRegression(random_state=2)
clf3 = SVC(probability=True, random_state=3)

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('lr', clf2), 
    ('svc', clf3)],
    voting='soft'  # use 'soft' for probability-based voting
)

# Combine training data (you may choose to create a stacked dataset instead)
X_combined = np.vstack((X1_train, X2_train, X3_train))
y_combined = np.concatenate((y1_train, y2_train, y3_train))

# Fit the voting classifier on the combined training dataset
voting_clf.fit(X_combined, y_combined)

# Evaluate the ensemble on combined test datasets
X_test_combined = np.vstack((X1_test, X2_test, X3_test))
y_test_combined = np.concatenate((y1_test, y2_test, y3_test))
accuracy = voting_clf.score(X_test_combined, y_test_combined)

print(f'Ensemble model accuracy: {accuracy:.2f}')
