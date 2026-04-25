
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Generate sample data for demonstration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.3, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.3, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Initialize the classifiers
classifier1 = LogisticRegression()
classifier2 = RandomForestClassifier()
classifier3 = SVC(probability=True)

# Train each classifier on its respective dataset
classifier1.fit(X_train1, y_train1)
classifier2.fit(X_train2, y_train2)
classifier3.fit(X_train3, y_train3)

# Create an ensemble using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('lr', classifier1), 
    ('rf', classifier2), 
    ('svc', classifier3)
], voting='soft')  # Use 'soft' to consider predicted probabilities

# Fit the ensemble model on the first dataset (or aggregate the datasets if needed)
ensemble_model.fit(X_train1, y_train1)

# Make predictions on the test set
predictions = ensemble_model.predict(X_test1)

# Evaluate the ensemble model
accuracy = ensemble_model.score(X_test1, y_test1)
print(f'Ensemble model accuracy: {accuracy:.2f}')
