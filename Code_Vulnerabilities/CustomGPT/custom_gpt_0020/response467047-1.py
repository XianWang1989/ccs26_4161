
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=0)
X2, y2 = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=1)
X3, y3 = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=2)

# Train/test split for each dataset
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=0)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=1)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=2)

# Initialize classifiers for each dataset
clf1 = DecisionTreeClassifier(random_state=0)
clf2 = RandomForestClassifier(random_state=1)
clf3 = LogisticRegression(random_state=2)

# Fit the classifiers on the corresponding datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1),
    ('rf', clf2),
    ('lr', clf3)],
    voting='hard')  # Use 'soft' for probabilities averaging

# Fit the voting classifier on one of the datasets
# Here, we can choose any of the datasets you would like to utilize for fitting
voting_clf.fit(X1_train, y1_train)

# Evaluate individual classifiers on the test sets
for i, (X_test, y_test, clf) in enumerate(zip([X1_test, X2_test, X3_test], [y1_test, y2_test, y3_test], [clf1, clf2, clf3]), start=1):
    y_pred = clf.predict(X_test)
    print(f"Classifier {i} Accuracy: {accuracy_score(y_test, y_pred)}")

# Evaluate the ensemble classifier on the first dataset's test set
ensemble_pred = voting_clf.predict(X1_test)
print("Ensemble Classifier Accuracy:", accuracy_score(y1_test, ensemble_pred))
