
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate sample datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Create individual classifiers
clf1 = RandomForestClassifier()
clf2 = SVC(probability=True)  # Set probability=True for soft voting
clf3 = LogisticRegression()

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[('rf', clf1), ('svc', clf2), ('lr', clf3)], voting='soft')

# Fit individual models
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Fit the voting classifier using combined predictions
# Here we use the models' predictions on the test set for evaluation
preds1 = clf1.predict(X1_test)
preds2 = clf2.predict(X2_test)
preds3 = clf3.predict(X3_test)

# Stack predictions and reshape
preds = np.column_stack((preds1, preds2, preds3))

# Fit the voting classifier on the combined predictions
voting_clf.fit(preds, y1_test)  # Use y1_test as the ground truth

# Make final predictions
final_preds = voting_clf.predict(preds)

# Evaluate accuracy
accuracy = accuracy_score(y1_test, final_preds)
print(f'Ensemble Accuracy: {accuracy:.2f}')
