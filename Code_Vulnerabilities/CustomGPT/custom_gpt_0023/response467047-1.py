
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Generate sample datasets (replace with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Train different classifiers on each dataset
model1 = DecisionTreeClassifier()
model2 = RandomForestClassifier()
model3 = SVC(probability=True)

model1.fit(X_train1, y_train1)
model2.fit(X_train2, y_train2)
model3.fit(X_train3, y_train3)

# Create a Voting Classifier
voting_classifier = VotingClassifier(estimators=[
    ('tree', model1), 
    ('forest', model2), 
    ('svc', model3)
], voting='soft')  # Use 'soft' for probability-based voting

# Fit the ensemble on a combined dataset (or you can use one of the datasets)
X_combined = np.vstack((X_train1, X_train2, X_train3))
y_combined = np.concatenate((y_train1, y_train2, y_train3))

voting_classifier.fit(X_combined, y_combined)

# Predict on the test datasets
predictions1 = voting_classifier.predict(X_test1)
predictions2 = voting_classifier.predict(X_test2)
predictions3 = voting_classifier.predict(X_test3)

print(f"Predictions for dataset 1: {predictions1}")
print(f"Predictions for dataset 2: {predictions2}")
print(f"Predictions for dataset 3: {predictions3}")
