
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers for each dataset
clf1 = DecisionTreeClassifier()
clf2 = RandomForestClassifier()
clf3 = LogisticRegression()

# Train each classifier on its respective dataset
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1), 
    ('rf', clf2), 
    ('lr', clf3)],
    voting='hard')  # Use 'soft' for probability-based voting

# Combine predictions using the Voting Classifier
X_combined = np.concatenate((X1_test, X2_test, X3_test))
y_combined = np.concatenate((y1_test, y2_test, y3_test))

# Fit Voting Classifier on the combined training data
voting_clf.fit(X_combined, y_combined)

# Make predictions
y_pred = voting_clf.predict(X_combined)

# Evaluate model
accuracy = accuracy_score(y_combined, y_pred)
print(f'Ensembled Model Accuracy: {accuracy:.2f}')
