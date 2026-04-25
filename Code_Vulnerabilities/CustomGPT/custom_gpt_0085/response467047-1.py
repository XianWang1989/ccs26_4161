
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize individual classifiers
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()
model3 = RandomForestClassifier()

# Train the classifiers
model1.fit(X_train1, y_train1)
model2.fit(X_train2, y_train2)
model3.fit(X_train3, y_train3)

# Create a VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('lr', model1), 
    ('dt', model2), 
    ('rf', model3)
], voting='soft')  # Use 'soft' for probability-based voting

# Train the ensemble model on one of the datasets (or on a combined dataset)
X_train_combined = np.concatenate((X_train1, X_train2, X_train3))
y_train_combined = np.concatenate((y_train1, y_train2, y_train3))

ensemble_model.fit(X_train_combined, y_train_combined)

# Make predictions
predictions = ensemble_model.predict(X_test1)  # Change as needed for test dataset

# Evaluate predictions
print(predictions)
