
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=0)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=1)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=2)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=0)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=1)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=2)

# Create classifiers for each dataset
clf1 = SVC(probability=True)
clf2 = RandomForestClassifier()
clf3 = LogisticRegression()

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble model with VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('svc', clf1),
    ('rf', clf2),
    ('lr', clf3)],
    voting='soft')  # Use 'soft' for probability-based voting

# Optionally, fit the ensemble on combined data
# Here, we're creating a combined dataset for demonstration
X_combined = np.concatenate((X1_train, X2_train, X3_train))
y_combined = np.concatenate((y1_train, y2_train, y3_train))
voting_clf.fit(X_combined, y_combined)

# Evaluate the ensemble
accuracy = voting_clf.score(np.concatenate((X1_test, X2_test, X3_test)),
                             np.concatenate((y1_test, y2_test, y3_test)))

print(f'Ensemble model accuracy: {accuracy:.2f}')
