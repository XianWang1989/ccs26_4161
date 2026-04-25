
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and validation sets
X1_train, X1_val, y1_train, y1_val = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_val, y2_train, y2_val = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_val, y3_train, y3_val = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define classifiers for each dataset
clf1 = RandomForestClassifier(random_state=1)
clf2 = LogisticRegression(random_state=2)
clf3 = SVC(probability=True, random_state=3)

# Fit models on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('lr', clf2),
    ('svc', clf3)
], voting='soft')

# Combine predictions
# Evaluate each classifier on the same validation set
val_preds1 = clf1.predict(X1_val)
val_preds2 = clf2.predict(X2_val)
val_preds3 = clf3.predict(X3_val)

# Stack predictions
stacked_preds = np.vstack((val_preds1, val_preds2, val_preds3)).T

# Fit the voting classifier with the stacked predictions
voting_clf.fit(stacked_preds, y1_val)  # Using y1_val as an example

# Final prediction
final_prediction = voting_clf.predict(stacked_preds)

print("Final predictions:", final_prediction)
