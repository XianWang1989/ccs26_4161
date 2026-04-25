
from sklearn.ensemble import VotingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=0)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=0)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=0)

# Train classifiers
clf1 = DecisionTreeClassifier().fit(X1_train, y1_train)
clf2 = SVC(probability=True).fit(X2_train, y2_train)
clf3 = LogisticRegression().fit(X3_train, y3_train)

# Create an ensemble classifier
voting_clf = VotingClassifier(estimators=[('dt', clf1), ('svc', clf2), ('lr', clf3)], voting='soft')

# Fit ensemble classifier on combined data
import numpy as np
X_combined = np.concatenate((X1, X2, X3))
y_combined = np.concatenate((y1, y2, y3))

voting_clf.fit(X_combined, y_combined)

# Predict
predictions = voting_clf.predict(X_combined)
print(predictions)
