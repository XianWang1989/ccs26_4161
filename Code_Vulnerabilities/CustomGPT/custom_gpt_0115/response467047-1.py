
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train different classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2)
clf3 = DecisionTreeClassifier(random_state=3)

clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble using VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('dt', clf3)
], voting='soft')  # use 'soft' voting for probability-based predictions

# Fit on combined training data
X_combined_train = np.vstack((X1_train, X2_train, X3_train))
y_combined_train = np.hstack((y1_train, y2_train, y3_train))

voting_clf.fit(X_combined_train, y_combined_train)

# Evaluate on combined test data
X_combined_test = np.vstack((X1_test, X2_test, X3_test))
y_combined_test = np.hstack((y1_test, y2_test, y3_test))

accuracy = voting_clf.score(X_combined_test, y_combined_test)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
