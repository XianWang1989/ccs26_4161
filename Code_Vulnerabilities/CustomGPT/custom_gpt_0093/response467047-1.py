
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers
clf1 = DecisionTreeClassifier(random_state=1)
clf2 = RandomForestClassifier(random_state=2)
clf3 = SVC(probability=True, random_state=3)

# Train classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble of trained classifiers
voting_clf = VotingClassifier(estimators=[('dt', clf1), ('rf', clf2), ('svc', clf3)], voting='soft')

# Combine datasets for ensemble training
X_combined = np.vstack((X1_train, X2_train, X3_train))
y_combined = np.concatenate((y1_train, y2_train, y3_train))

# Train the ensemble classifier
voting_clf.fit(X_combined, y_combined)

# Evaluate ensemble performance
X_test_combined = np.vstack((X1_test, X2_test, X3_test))
y_test_combined = np.concatenate((y1_test, y2_test, y3_test))

y_pred = voting_clf.predict(X_test_combined)
accuracy = accuracy_score(y_test_combined, y_pred)

print(f'Ensemble Accuracy: {accuracy:.2f}')
