
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
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual models on each dataset
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()
model3 = RandomForestClassifier()

model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
voting_model = VotingClassifier(estimators=[
    ('lr', model1), 
    ('dt', model2), 
    ('rf', model3)],
    voting='hard'  # You can also use 'soft' for probability-based voting
)

# Train the ensemble model using the predictions from each dataset
# Using the training set predictions as features
X_train_combined = np.hstack((
    model1.predict(X1_train).reshape(-1, 1),
    model2.predict(X2_train).reshape(-1, 1),
    model3.predict(X3_train).reshape(-1, 1)
))

# Fit the ensemble model on combined training predictions
voting_model.fit(X_train_combined, y1_train)  # Use any of the labels

# Test the ensemble model
X_test_combined = np.hstack((
    model1.predict(X1_test).reshape(-1, 1),
    model2.predict(X2_test).reshape(-1, 1),
    model3.predict(X3_test).reshape(-1, 1)
))

# Make predictions
ensemble_predictions = voting_model.predict(X_test_combined)

print("Ensemble Predictions:", ensemble_predictions)
