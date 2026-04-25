
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import train_test_split

# Step 1: Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Step 2: Split into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Step 3: Create classifiers for each dataset
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)
clf3 = RandomForestClassifier(random_state=3)

# Step 4: Fit the classifiers
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Step 5: Use VotingClassifier to ensemble models
voting_clf = VotingClassifier(estimators=[
    ('rf1', clf1),
    ('gb', clf2),
    ('rf2', clf3)],
    voting='hard')

# Step 6: Fit the voting classifier on one of the datasets
# Here we're using dataset 1 for simplicity
voting_clf.fit(X1_train, y1_train)

# Step 7: Predictions
predictions = voting_clf.predict(X1_test)

# Step 8: Evaluate the ensemble model
accuracy = voting_clf.score(X1_test, y1_test)
print("Ensemble Model Accuracy: ", accuracy)
