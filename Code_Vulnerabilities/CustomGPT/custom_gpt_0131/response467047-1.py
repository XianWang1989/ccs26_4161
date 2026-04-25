
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Assuming you have your datasets created with `make_classification` for this example
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize your classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = LogisticRegression(random_state=2)
clf3 = SVC(probability=True, random_state=3)

# Fit the models on their respective training datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble model with VotingClassifier
voting_clf = VotingClassifier(estimators=[('rf', clf1), ('lr', clf2), ('svc', clf3)], voting='soft')

# Fit the voting classifier on the combined training set (you need to take care of this)
X_combined_train = np.vstack((X1_train, X2_train, X3_train))
y_combined_train = np.concatenate((y1_train, y2_train, y3_train))

voting_clf.fit(X_combined_train, y_combined_train)

# Predict using the combined ensemble model
X_combined_test = np.vstack((X1_test, X2_test, X3_test))
y_combined_test = np.concatenate((y1_test, y2_test, y3_test))
y_pred = voting_clf.predict(X_combined_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_combined_test, y_pred)
print("Ensemble Model Accuracy: {:.2f}%".format(accuracy * 100))
