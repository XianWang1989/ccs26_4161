
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Create synthetic datasets for demonstration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
clf1 = DecisionTreeClassifier()
clf2 = RandomForestClassifier()
clf3 = SVC(probability=True)

clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1), 
    ('rf', clf2), 
    ('svc', clf3)
], voting='soft')  # Use 'soft' for probability-based voting

# Fit the ensemble on the combined validation set
X_combined = np.vstack((X1_test, X2_test, X3_test))
y_combined = np.hstack((y1_test, y2_test, y3_test))

voting_clf.fit(X_combined, y_combined)

# Make predictions
predictions = voting_clf.predict(X_combined)

# Evaluate the model
accuracy = np.mean(predictions == y_combined)
print("Ensemble Accuracy:", accuracy)
