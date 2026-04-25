
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Simulate three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train classifiers on each dataset
clf1 = LogisticRegression()
clf1.fit(X1_train, y1_train)

clf2 = DecisionTreeClassifier()
clf2.fit(X2_train, y2_train)

clf3 = RandomForestClassifier()
clf3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('lr', clf1), ('dt', clf2), ('rf', clf3)],
    voting='hard'  # Use 'soft' for probabilities
)

# Fit the ensemble model using one of the datasets (or combine inputs)
ensemble_model.fit(X1_train, y1_train)  # You can choose any training set

# Make predictions
predictions = ensemble_model.predict(X1_test)

# Evaluate accuracy
accuracy = accuracy_score(y1_test, predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
