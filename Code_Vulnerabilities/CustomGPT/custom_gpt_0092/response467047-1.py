
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers on different datasets
clf1 = DecisionTreeClassifier()
clf1.fit(X_train1, y_train1)

clf2 = RandomForestClassifier()
clf2.fit(X_train2, y_train2)

clf3 = LogisticRegression()
clf3.fit(X_train3, y_train3)

# Create an ensemble using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('dt', clf1),
    ('rf', clf2),
    ('lr', clf3)
], voting='hard')

# Train the ensemble model on the first dataset (as an example)
ensemble_model.fit(X_train1, y_train1)

# Make predictions on test dataset
predictions = ensemble_model.predict(X_test1)

# Optional: Evaluate the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test1, predictions)
print(f"Ensemble Model Accuracy: {accuracy:.2f}")
