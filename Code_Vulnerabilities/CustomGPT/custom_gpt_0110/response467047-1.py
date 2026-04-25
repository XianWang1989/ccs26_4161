
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

# Split into train and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers for each dataset
clf1 = RandomForestClassifier()
clf2 = SVC(probability=True)
clf3 = LogisticRegression()

# Fit the classifiers
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)
], voting='soft')  # Use 'hard' for majority voting or 'soft' for probability-based

# Fit the voting classifier
X_combined_train = np.concatenate((X_train1, X_train2, X_train3))
y_combined_train = np.concatenate((y_train1, y_train2, y_train3))
voting_clf.fit(X_combined_train, y_combined_train)

# Evaluate on test set (you can combine test datasets similarly if needed)
X_combined_test = np.concatenate((X_test1, X_test2, X_test3))
y_combined_test = np.concatenate((y_test1, y_test2, y_test3))
accuracy = voting_clf.score(X_combined_test, y_combined_test)

print(f'Ensemble accuracy: {accuracy:.2f}')
