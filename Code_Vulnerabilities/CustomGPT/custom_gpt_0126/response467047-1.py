
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the first dataset into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=0)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=0)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=0)

# Define classifiers
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()
clf3 = RandomForestClassifier()

# Fit classifiers on their respective datasets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create Voting Classifier
voting_clf = VotingClassifier(estimators=[('lr', clf1), ('dt', clf2), ('rf', clf3)], voting='hard')

# Fit Voting Classifier on combined datasets
X_combined = np.vstack((X_train1, X_train2, X_train3))
y_combined = np.hstack((y_train1, y_train2, y_train3))
voting_clf.fit(X_combined, y_combined)

# Evaluate
Y_pred = voting_clf.predict(np.vstack((X_test1, X_test2, X_test3)))
true_labels = np.hstack((y_test1, y_test2, y_test3))
accuracy = accuracy_score(true_labels, Y_pred)

print(f'Accuracy of Voting Classifier: {accuracy:.2f}')
