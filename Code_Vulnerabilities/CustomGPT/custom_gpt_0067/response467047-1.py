
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual models
model1 = RandomForestClassifier()
model2 = SVC(probability=True)
model3 = LogisticRegression()

model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create an ensemble of the models
voting_classifier = VotingClassifier(
    estimators=[
        ('rf', model1), 
        ('svc', model2), 
        ('lr', model3)
    ], 
    voting='soft'  # Use 'soft' for probability-based voting
)

# Fit the ensemble on one of the datasets (you can choose any)
voting_classifier.fit(X1_train, y1_train)

# Make predictions
predictions = voting_classifier.predict(X1_test)
print("Ensemble predictions:", predictions)
